import os
from cognite.client import CogniteClient, ClientConfig
from cognite.client.credentials import OAuthInteractive
from dotenv import load_dotenv

load_dotenv()

CDF_CLUSTER           = os.environ['CDF_CLUSTER']
COGNITE_PROJECT       = os.environ['COGNITE_PROJECT']
COGNITE_CLIENT_ID     = os.environ['COGNITE_CLIENT_ID']
COGNITE_TENANT_ID     = os.environ['COGNITE_TENANT_ID']
DATA_SET_XID          = os.environ['COGNITE_DATA_SET_XID']
COGNITE_CLIENT_NAME   = "Python client"

def get_client():
    oauth_provider = OAuthInteractive(
        authority_url=f"https://login.microsoftonline.com/{COGNITE_TENANT_ID}",
        client_id=COGNITE_CLIENT_ID,
        scopes=[f"https://{CDF_CLUSTER}.cognitedata.com/.default"])
    config = ClientConfig(
        client_name="my-client",
        base_url=f"https://{CDF_CLUSTER}.cognitedata.com",
        project=COGNITE_PROJECT,
        credentials=oauth_provider)
    cognite_client = CogniteClient(config)
    return cognite_client
