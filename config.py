from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get API key from environment variables
Open_router_API_KEY = os.getenv('open_Router_API_KEY')

if Open_router_API_KEY is None:
    raise ValueError("Open_router_API_KEY not found in environment variables")

Groq_API_KEY = os.getenv('Groq_API_KEY')

Gemini_API_KEY = os.getenv('GEMINI_API_KEY')

Serper_API_KEY = os.getenv('Serper_API_KEY')

