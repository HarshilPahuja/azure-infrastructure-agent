from fastmcp import FastMCP
from azure_client import resource_client

mcp = FastMCP("Azure VM Agent")


@mcp.tool
def hello(name: str) -> str:
    """Say hello to someone."""
    return f"Hello {name}! MCP is working!"

@mcp.tool
def create_resource_group(
    name: str,
    location: str
):
    """
    Creates an Azure Resource Group.
    """

    rg = resource_client.resource_groups.create_or_update(
        name,
        {
            "location": location
        }
    )

    return {
        "status": "success",
        "resource_group": rg.name,
        "location": rg.location
    }