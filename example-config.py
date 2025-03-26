# Configuration file for Obsidian Summarizer
# Copy this file to config.py and update with your values

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# OpenAI Configuration
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")  # Will be loaded from .env file
OPENAI_MODEL = "gpt-4"  # Options: "gpt-4", "gpt-3.5-turbo" (adjust based on your needs)

# Obsidian Vault Paths (will be loaded from .env file)
DAILY_VAULT_PATH = os.getenv("DAILY_VAULT_PATH")  # Path to your daily notes
TO_LEARN_VAULT_PATH = os.getenv("TO_LEARN_VAULT_PATH")  # Path where summaries will be saved

# Optional: Advanced Configuration
# MODEL_MAX_TOKENS = 4000  # Uncomment to set a custom token limit
# TEMPERATURE = 0.7  # Uncomment to adjust model creativity (0.0 - 1.0)