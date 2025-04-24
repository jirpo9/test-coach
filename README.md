# test-coach

A new project currently under development.

## Overview

This project implements an AI-powered testing and code-fixing server using FastMCP and OpenAI. It provides tools to generate tests, run them under coverage, and suggest code fixes.

## Setup

1. Create and activate a Python virtual environment:
   ```bash
   python -m virtualenv .venv
   source .venv/bin/activate    # On Windows: `.\\.venv\\Scripts\\activate`
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

## How it works

- **Server (`fastmcp_server`)** exposes three tools via standard I/O:
  - `generate_tests(module: str) -> str`  
    Generates pytest tests for a given Python module using the OpenAI ChatCompletion API.
  - `run_tests() -> dict`  
    Runs tests under coverage, produces a JSON coverage report, and returns it.
  - `fix_code(failing_test: str, error: str) -> str`  
    Prompts OpenAI to suggest code or test fixes so that pytest passes.

- **Pipe (`fastmcp_server/pipe.py`)** handles communication with the OpenAI API:
  - Loads `OPENAI_API_KEY` and optional `OPENAI_MODEL` from `.env`.
  - Defines `codex_query(prompt, temperature)` wrapping `openai.ChatCompletion.create`.

- **Tools (`fastmcp_server/tools.py`)** implement the logic of each tool, decorated with `@mcp.tool()`.

- **Server entrypoint (`fastmcp_server/server.py`)**:
  - Imports and registers all tools, then calls `mcp.run()` to start listening on stdio.

- **Sample library (`sample_lib/calculator.py`)** provides simple functions `add(a, b)` and
  `divide(a, b)` (with a deliberate `ZeroDivisionError` on `b=0`) to demonstrate the workflow.

## Usage Example

1. Start the FastMCP server:
   ```bash
   python -m fastmcp_server.server
   ```
2. Generate tests for the sample module in another terminal:
   ```bash
   mcp-cli call generate_tests \
     --server stdio://$(pgrep -f fastmcp_server.server) \
     --json '{"module":"sample_lib.calculator"}'
   ```
3. Run tests and retrieve coverage:
   ```bash
   mcp-cli call run_tests --server stdio://$(pgrep -f fastmcp_server.server)
   ```


## Tento projekt, nazvaný "test-coach", je nástroj pro automatizované testování a opravy kódu s využitím AI (konkrétně OpenAI API). Hlavní funkce zahrnují:

### Generování automatických testů pro Python moduly
### Spouštění testů s analýzou pokrytí kódu
### Navrhování oprav kódu na základě neúspěšných testů a chybových hlášek



**3. Použití serveru
Alternativně můžete server spustit přímo:
python -m fastmcp_server.server
Tím se spustí server, který naslouchá na stdin/stdout, což je užitečné pro integraci s jinými nástroji.
