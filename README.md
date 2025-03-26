# Obsidian Summarizer

A Python script that automatically summarizes your daily Obsidian notes and creates a learning vault with summaries and glossaries.

## Features

- Processes notes from your daily vault
- Creates AI-powered summaries with key concepts
- Generates a glossary of important terms
- Automatically cleans up processed notes
- Runs on a schedule (default: 6 AM daily)

## Setup

1. Clone this repository
2. Create a virtual environment and activate it:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up your configuration:
   - Copy `.env.example` to `.env`
   - Update the values in `.env` with your:
     - OpenAI API key
     - Path to your daily notes vault
     - Path to where you want summaries saved
   ```bash
   cp .env.example .env
   # Edit .env with your preferred editor
   ```

## Usage

The script can be run in two ways:

1. Manual execution:
   ```bash
   python obsidian-summarizer.py
   ```

2. Automated scheduling (recommended):
   ```bash
   # Make the runner script executable
   chmod +x run_summarizer.sh
   ```

   ### For macOS Users (Recommended):
   Create a launchd job to run the script automatically:

   1. Create a new file at `~/Library/LaunchAgents/com.user.obsidian-summarizer.plist`:
   ```xml
   <?xml version="1.0" encoding="UTF-8"?>
   <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
   <plist version="1.0">
   <dict>
       <key>Label</key>
       <string>com.user.obsidian-summarizer</string>
       <key>ProgramArguments</key>
       <array>
           <string>/full/path/to/obsidian-summarizer/run_summarizer.sh</string>
       </array>
       <key>StartCalendarInterval</key>
       <dict>
           <key>Hour</key>
           <integer>6</integer>
           <key>Minute</key>
           <integer>0</integer>
       </dict>
       <key>StandardOutPath</key>
       <string>/full/path/to/obsidian-summarizer/cron.log</string>
       <key>StandardErrorPath</key>
       <string>/full/path/to/obsidian-summarizer/cron.log</string>
       <key>RunAtLoad</key>
       <true/>
       <key>StartOnMount</key>
       <true/>
       <key>KeepAlive</key>
       <dict>
           <key>SuccessfulExit</key>
           <false/>
       </dict>
   </dict>
   </plist>
   ```
   
   2. Replace `/full/path/to/obsidian-summarizer/` with your actual path
   3. Load the job:
   ```bash
   launchctl load ~/Library/LaunchAgents/com.user.obsidian-summarizer.plist
   ```

   The job will now run:
   - At 6 AM daily if your computer is awake
   - When your computer wakes up if it was asleep at 6 AM
   - When your computer starts up if it was off at 6 AM

   To manage the job:
   ```bash
   # Check if it's running
   launchctl list | grep obsidian

   # View logs
   tail -f /full/path/to/obsidian-summarizer/cron.log

   # Stop the job
   launchctl unload ~/Library/LaunchAgents/com.user.obsidian-summarizer.plist

   # Start the job again
   launchctl load ~/Library/LaunchAgents/com.user.obsidian-summarizer.plist
   ```

   ### For Linux/Other Unix Users:
   Add to crontab to run at 6 AM daily:
   ```bash
   # Add to crontab (runs at 6 AM daily)
   crontab -e

   # Add this line (replace paths with your actual paths):
   0 6 * * * /full/path/to/obsidian-summarizer/run_summarizer.sh >> /full/path/to/obsidian-summarizer/cron.log 2>&1
   ```

   Notes about the cron setup:
   - Create the log file: `touch /full/path/to/obsidian-summarizer/cron.log`
   - The `2>&1` ensures both normal output and errors are saved to the log file
   - View logs using: `tail -f /full/path/to/obsidian-summarizer/cron.log`

## How It Works

1. At 6 AM each day, the script:
   - Finds all notes created the previous day
   - Generates a comprehensive summary
   - Creates a glossary of important terms
   - Saves the summary to your learning vault
   - Cleans up the processed notes

## Security Note

This repository uses environment variables for sensitive information. Never commit your `.env` file or `config.py` with real values. The example files provided are templates only.
