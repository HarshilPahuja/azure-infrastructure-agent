from app import mcp

print("SERVER MCP ID:", id(mcp))

import tools.resource_groups
import tools.storage_accounts

if __name__ == "__main__":
    mcp.run()