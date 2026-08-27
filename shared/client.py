from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env"))

api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise RuntimeError("GROQ_API_KEY is not set. Add it to the project .env file.")

groq_client = OpenAI(
    api_key=api_key,
    base_url="https://api.groq.com/openai/v1"
)
