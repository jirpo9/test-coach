"""Tool definitions for fastmcp server."""
from fastmcp import mcp
from .pipe import codex_query
import subprocess
import json
import tempfile
import pathlib

@mcp.tool()
def generate_tests(module: str) -> str:
    """Generate pytest tests for the given module path."""
    path = pathlib.Path(module.replace('.', '/') + '.py')
    src = path.read_text()
    prompt = f"Write thorough pytest tests for:\n\n{src}"
    return codex_query(prompt)

@mcp.tool()
def run_tests() -> dict:
    """Run tests with coverage and return coverage data as JSON."""
    with tempfile.NamedTemporaryFile() as f:
        subprocess.run(["coverage", "run", "-m", "pytest", "-q"], check=False)
        subprocess.run(["coverage", "json", "-o", f.name], check=False)
        return json.load(open(f.name))

@mcp.tool()
def fix_code(failing_test: str, error: str) -> str:
    """Suggest fixes to code or tests that will pass pytest."""
    prompt = (
        f"Fix code (or test) so that pytest passes.\n"
        f"Failing test:\n{failing_test}\n"
        f"Error:\n{error}"
    )
    return codex_query(prompt, temperature=0)