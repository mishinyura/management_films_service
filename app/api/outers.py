from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("API_KEY")

if not api_key:
    raise ValueError("API_KEY is not set")