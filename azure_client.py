import os

from dotenv import load_dotenv

from azure.identity import DefaultAzureCredential

from azure.mgmt.resource.resources import ResourceManagementClient
load_dotenv()

subscription_id = os.getenv("AZURE_SUBSCRIPTION_ID")

credential = DefaultAzureCredential()

resource_client = ResourceManagementClient(
    credential,
    subscription_id
)