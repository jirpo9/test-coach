# test-coach

A new project currently under development.

## Setup

1. Create and activate a Python virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate    # On Windows: `.\venv\Scripts\activate`
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Copy the example environment file and configure your variables:
   ```bash
   cp .env.example .env      # On Windows: `copy .env.example .env`
   # Then edit .env and set your values
   ```
4. (Optional) Remove any embedded credentials from Git config:
   ```bash
   git remote set-url origin https://github.com/$GITHUB_USER/test-coach.git
   ```

## Environment Variables

Store all sensitive keys and tokens in the `.env` file. See `.env.example` for required names.
