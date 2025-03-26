import os
import glob
import datetime
from openai import OpenAI
from config import OPENAI_API_KEY, DAILY_VAULT_PATH, TO_LEARN_VAULT_PATH, OPENAI_MODEL
from examples import FEW_SHOT_EXAMPLES
client = OpenAI(api_key=OPENAI_API_KEY)

def setup():
    """Initialize OpenAI API and ensure directories exist."""
    os.makedirs(TO_LEARN_VAULT_PATH, exist_ok=True)

def get_todays_files():
    """Get all files created today in the clippings vault."""    
    today = datetime.datetime.now().date()
    today_files = []

    for file_path in glob.glob(f"{DAILY_VAULT_PATH}/**/*.md", recursive=True):
        file_creation_time = datetime.datetime.fromtimestamp(
            os.path.getctime(file_path)
        ).date()

        if file_creation_time == today:
            today_files.append(file_path)

    return today_files

def get_previous_day_files():
    """Get all files created yesterday in the clippings vault."""    
    yesterday = (datetime.datetime.now() - datetime.timedelta(days=1)).date()
    yesterday_files = []

    for file_path in glob.glob(f"{DAILY_VAULT_PATH}/**/*.md", recursive=True):
        file_creation_time = datetime.datetime.fromtimestamp(
            os.path.getctime(file_path)
        ).date()

        if file_creation_time == yesterday:
            yesterday_files.append(file_path)

    return yesterday_files

def read_file_content(file_path):
    """Read the content of a file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return ""

def summarize_content(files):
    """Use OpenAI to summarize the content of files and create a glossary."""
    if not files:
        return "No files were created today."

    # Combine all file contents with their names
    combined_content = ""
    for file_path in files:
        file_name = os.path.basename(file_path)
        content = read_file_content(file_path)
        combined_content += f"## {file_name}\n\n{content}\n\n"

    # Prepare the prompt for OpenAI
    prompt = f"""
    {FEW_SHOT_EXAMPLES}
    
    Now, please analyze the following content from my notes and provide:
    
    1. A comprehensive summary that connects related ideas across all notes
    2. A glossary of important terms, phrases, concepts, and tools mentioned that would be valuable to learn more about
    
    Here are the notes:
    
    {combined_content}
    """

    try:
        response = client.chat.completions.create(model=OPENAI_MODEL,
        messages=[
            {"role": "system", "content": "You are a helpful assistant that summarizes technical content and identifies important concepts in AI, information security, operations security, machine learning, deep learning, AI agents, automation, programming, development, and related fields. You focus on creating clear, concise summaries and precise definitions."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=2000)
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error with OpenAI API: {e}")
        return f"Error generating summary: {e}"

def save_summary(summary):
    """Save the summary to the to_learn vault."""
    # Use yesterday's date for the summary since we're processing yesterday's files
    yesterday = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y-%m-%d")
    summary_file_path = os.path.join(TO_LEARN_VAULT_PATH, f"Daily Summary {yesterday}.md")

    # Format the summary with a nice header
    formatted_summary = f"""# Daily Summary for {yesterday}

{summary}
"""

    try:
        with open(summary_file_path, 'w', encoding='utf-8') as file:
            file.write(formatted_summary)
        print(f"Summary saved to {summary_file_path}")
    except Exception as e:
        print(f"Error saving summary: {e}")

def cleanup_processed_files(files_to_cleanup):
    """Delete the files that were just processed."""
    for file_path in files_to_cleanup:
        try:
            os.remove(file_path)
            print(f"Removed processed file: {file_path}")
        except Exception as e:
            print(f"Error removing {file_path}: {e}")

def process_daily_notes():
    """Main function to process notes for the day."""
    print(f"Running daily processing at {datetime.datetime.now()}")

    # Get yesterday's files
    yesterday_files = get_previous_day_files()
    print(f"Found {len(yesterday_files)} files from yesterday")

    # Summarize content and create glossary
    summary = summarize_content(yesterday_files)

    # Save the summary
    save_summary(summary)

    # Clean up the processed files
    cleanup_processed_files(yesterday_files)

def main():
    """Main entry point for the script."""
    setup()
    process_daily_notes()

if __name__ == "__main__":
    main()