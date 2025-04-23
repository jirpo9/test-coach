"""Configuration loader using python-dotenv."""

import os
from dotenv import load_dotenv

# Load variables from .env file into environment
load_dotenv()

# Environment variables
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
API_KEY = os.getenv('API_KEY')
DB_PASSWORD = os.getenv('DB_PASSWORD')

def show_config():
    """Prints which configuration variables are set."""
    print("Configuration status:")
    print(f"GITHUB_TOKEN = {'set' if GITHUB_TOKEN else 'not set'}")
    print(f"API_KEY      = {'set' if API_KEY else 'not set'}")
    print(f"DB_PASSWORD  = {'set' if DB_PASSWORD else 'not set'}")

if __name__ == '__main__':
    show_config()