from azure_client import resource_client

for rg in resource_client.resource_groups.list():
    print(rg.name)