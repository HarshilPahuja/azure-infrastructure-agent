from app import mcp
from azure_client import storage_client
print("STORAGE MCP ID:", id(mcp))
print("Loaded storage_accounts.py")
@mcp.tool
def create_storage_account(
    resource_group: str,
    account_name: str,
    location: str
):
    """
    Creates an Azure Storage Account.
    """

    try:

        poller = storage_client.storage_accounts.begin_create(

            resource_group,

            account_name,

            {
                "sku": {
                    "name": "Standard_LRS"
                },

                "kind": "StorageV2",

                "location": location
            }

        )

        account = poller.result()

        return {
            "success": True,
            "storage_account": account.name,
            "location": account.location
        }

    except Exception as e:

        return {
            "success": False,
            "error": str(e)
        }
    
@mcp.tool
def list_storage_accounts():
    """
    Lists all Storage Accounts.
    """

    try:

        accounts = storage_client.storage_accounts.list()

        return {

            "success": True,

            "storage_accounts": [

                {
                    "name": account.name,
                    "location": account.location,
                    "kind": account.kind
                }

                for account in accounts

            ]

        }

    except Exception as e:

        return {

            "success": False,
            "error": str(e)

        }
    

@mcp.tool
def delete_storage_account(
    resource_group: str,
    account_name: str
):
    """
    Deletes a Storage Account.
    """

    try:

        poller = storage_client.storage_accounts.begin_delete(

            resource_group,

            account_name

        )

        poller.result()

        return {

            "success": True,
            "message": f"Storage Account '{account_name}' deleted."

        }

    except Exception as e:

        return {

            "success": False,
            "error": str(e)

        }