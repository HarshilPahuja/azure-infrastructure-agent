from fastmcp import FastMCP

mcp = FastMCP("Azure VM Agent")


@mcp.tool
def hello(name: str) -> str:
    """Say hello to someone."""
    return f"Hello {name}! MCP is working!"