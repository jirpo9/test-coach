"""Entry point for fastmcp_server."""
from fastmcp import mcp
import fastmcp_server.tools  # noqa: register tools decorators

def main():
    """Run the fastmcp server listening on stdio."""
    mcp.run()

if __name__ == '__main__':
    main()