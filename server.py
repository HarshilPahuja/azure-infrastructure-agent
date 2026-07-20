from fastmcp import FastMCP
from azure_client import resource_client

mcp = FastMCP("Azure VM Agent")

@mcp.tool
def create_resource_group(name: str, location: str):
    """
    Creates an Azure Resource Group.
    """

    try:
        rg = resource_client.resource_groups.create_or_update(
            name,
            {
                "location": location
            }
        )

        return {
            "success": True,
            "resource_group": rg.name,
            "location": rg.location
        }

    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }

@mcp.tool
def list_resource_groups():
    """
    Lists all Azure Resource Groups.
    """

    try:
        groups = resource_client.resource_groups.list()

        return {
            "success": True,
            "resource_groups": [
                {
                    "name": rg.name,
                    "location": rg.location,
                    "id": rg.id
                }
                for rg in groups
            ]
        }

    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }

@mcp.tool
def delete_resource_group(name: str):
    """
    Deletes an Azure Resource Group.
    """

    try:
        poller = resource_client.resource_groups.begin_delete(name)
        poller.result()

        return {
            "success": True,
            "message": f"Resource Group '{name}' deleted successfully."
        }

    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }