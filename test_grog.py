import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Ensure the DEEPGRAM_API_KEY is correctly set in your environment variables
DEEPGRAM_API_KEY = os.getenv("DG_API_KEY")

# Check if the API key is loaded correctly
if not DEEPGRAM_API_KEY:
    raise ValueError("Deepgram API key not found in environment variables.")

print(DEEPGRAM_API_KEY)

