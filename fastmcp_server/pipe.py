"""Pipe wrapper for OpenAI ChatCompletion API."""
import os
from dotenv import load_dotenv
import openai

# Load environment variables from .env (if present)
load_dotenv()

# Configure API key and default model
openai.api_key = os.getenv('OPENAI_API_KEY')
MODEL = os.getenv('OPENAI_MODEL', 'gpt-3.5-turbo')

def codex_query(prompt: str, temperature: float = 0.1) -> str:
    """Send a prompt to the OpenAI ChatCompletion API and return the response."""
    response = openai.ChatCompletion.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=temperature,
    )
    # Extract and return the assistant's reply
    return response.choices[0].message.content.strip()