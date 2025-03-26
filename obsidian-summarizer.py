import os
import glob
import datetime
from openai import OpenAI
from config import OPENAI_API_KEY, DAILY_VAULT_PATH, TO_LEARN_VAULT_PATH
client = OpenAI(api_key=OPENAI_API_KEY)
# Configuration Change this
OPENAI_MODEL = "gpt-4o-2024-11-20"  # Or another model of your choice

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

    # Few shot examples to guide the model
    # Few-shot examples to guide the model
    few_shot_examples = """
    Example 1:
    
    Input notes:
    ## llm-training-techniques.md
    RLHF is becoming standard for aligning LLMs with human preferences. Started with InstructGPT, now used in Claude, GPT-4, etc. Key challenge is creating diverse, high-quality feedback data. Constitutional AI is an alternative that uses AI feedback instead of human labelers.
    
    ## vector-database-comparison.md
    Compared Pinecone, Weaviate, and Milvus for my RAG application. Pinecone has simple API but higher cost. Weaviate offers hybrid search capabilities. Milvus scales better for my expected data volume. Going with Milvus for now.
    
    Example summary:
    Today's notes covered two AI infrastructure topics: (1) LLM training techniques focusing on RLHF as the standard alignment method and Constitutional AI as an emerging alternative; (2) A comparison of vector databases (Pinecone, Weaviate, and Milvus) for RAG applications, with Milvus selected for its superior scaling capabilities.
    
    Example glossary:
    * RLHF (Reinforcement Learning from Human Feedback) - A technique to align LLMs with human preferences using human evaluations of model outputs
    * Constitutional AI - An alignment approach that uses AI feedback instead of human labelers to train models according to constitutional principles
    * RAG (Retrieval-Augmented Generation) - A technique that enhances LLM outputs by retrieving relevant context from external knowledge sources
    * Vector Database - Specialized database optimized for storing and querying vector embeddings
    * Pinecone - A managed vector database service with simple API but higher costs
    * Weaviate - A vector database with hybrid search capabilities combining vector and keyword search
    * Milvus - An open-source vector database with strong scaling capabilities for large data volumes
    
    Example 2:
    
    Input notes:
    ## autonomous-agent-architecture.md
    Designed a multi-agent system using ReAct framework. Agents maintain working memory, use tools including web search and code execution. Planning agent coordinates 3 specialist agents. Communication through structured JSON. Need to implement better conflict resolution.
    
    ## zero-day-vulnerabilities-research.md
    Read about recent zero-day in Chrome's V8 engine. Attackers using type confusion to achieve remote code execution. Defense-in-depth strategies essential: sandboxing, privilege separation, ASLR. Added Synk scanning to our CI/CD pipeline for early detection.
    
    ## solo-dev-productivity.md
    Time-blocking technique working well for deep work. 90-minute blocks with no distractions. Using Pomodoro (25/5) for administrative tasks. Weekly review crucial for course correction. Need to improve estimation - consistently underestimating tasks by ~30%.
    
    Example summary:
    Today's notes covered three areas: (1) Architectural design for an autonomous multi-agent system using the ReAct framework with specialized agents communicating via JSON; (2) Research on zero-day vulnerabilities, specifically in Chrome's V8 engine, and implemented defense strategies including Synk scanning in CI/CD; (3) Productivity techniques for solo development including time-blocking, Pomodoro for admin tasks, and weekly reviews, with a note about estimation challenges.
    
    Example glossary:
    * ReAct (Reasoning + Acting) - A framework enabling LLM agents to combine reasoning with action-taking in interactive environments
    * Multi-agent system - A system where multiple AI agents collaborate to solve problems, often with specialized roles
    * Working memory - A temporary storage and manipulation space for information an agent is currently processing
    * Zero-day vulnerability - A software security flaw unknown to the vendor that hackers can exploit before it's patched
    * Type confusion - A memory vulnerability where a program accesses memory using an incompatible type
    * Defense-in-depth - A cybersecurity approach using multiple protective mechanisms rather than a single strong barrier
    * ASLR (Address Space Layout Randomization) - A security technique that randomizes memory addresses to prevent exploitation
    * CI/CD pipeline - Continuous Integration/Continuous Deployment automation for software delivery
    * Time-blocking - A productivity technique allocating specific time periods for focused work on particular tasks
    * Pomodoro Technique - A time management method using 25-minute focused work periods separated by short breaks
    """
    # Prepare the prompt for OpenAI
    prompt = f"""
    {few_shot_examples}
    
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