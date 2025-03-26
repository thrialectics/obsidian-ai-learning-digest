# example-config.py - Copy to config.py and update with your details
import os
from dotenv import load_dotenv

load_dotenv()

# These values should be set in your .env file
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")  # Your OpenAI API key
DAILY_VAULT_PATH = os.getenv("DAILY_VAULT_PATH")  # Path to your daily clippings vault
TO_LEARN_VAULT_PATH = os.getenv("TO_LEARN_VAULT_PATH")  # Path to your learning vault
OPENAI_MODEL = "gpt-4o-2024-11-20"  # Or another model of your choice