import os
from pathlib import Path
from dotenv import load_dotenv

# Resolve the path to the project root (one level up from the bot/ folder)
BASE_DIR = Path(__file__).resolve().parent.parent
ENV_PATH = BASE_DIR / ".env.bot.secret"

# Load the environment variables from the specific path
load_dotenv(dotenv_path=ENV_PATH)

# Export the variables for use in other modules
BOT_TOKEN = os.getenv("BOT_TOKEN")
LMS_API_URL = os.getenv("LMS_API_URL")
LMS_API_KEY = os.getenv("LMS_API_KEY")
LLM_API_KEY = os.getenv("LLM_API_KEY")
LLM_API_BASE_URL = os.getenv("LLM_API_BASE_URL")
LLM_API_MODEL = os.getenv("LLM_API_MODEL")



# Quick validation to ensure it loaded correctly when starting
if not BOT_TOKEN:
    print(f"Warning: BOT_TOKEN not found. Make sure {ENV_PATH} exists.")