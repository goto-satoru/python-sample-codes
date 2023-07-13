import os
from cognite.client import CogniteClient, ClientConfig
from cognite.client.credentials import OAuthClientCredentials
from dotenv import load_dotenv

load_dotenv()

CDF_CLUSTER           = os.environ['CDF_CLUSTER']
COGNITE_PROJECT       = os.environ['COGNITE_PROJECT']
COGNITE_CLIENT_ID     = os.environ['COGNITE_CLIENT_ID']
COGNITE_TENANT_ID     = os.environ['COGNITE_TENANT_ID']
COGNITE_CLIENT_SECRET = os.environ['COGNITE_CLIENT_SECRET']
DATA_SET_XID          = os.environ['COGNITE_DATA_SET_XID']
COGNITE_CLIENT_NAME   = "Python client"

def get_client():
    credentials = OAuthClientCredentials(
                token_url=f"https://login.microsoftonline.com/{COGNITE_TENANT_ID}/oauth2/v2.0/token",
                client_id=COGNITE_CLIENT_ID,
                client_secret=COGNITE_CLIENT_SECRET,
                scopes=[f"https://{CDF_CLUSTER}.cognitedata.com/.default"])
    client_config = ClientConfig(
                client_name=COGNITE_CLIENT_NAME,
                base_url=f"https://{CDF_CLUSTER}.cognitedata.com",
                project=COGNITE_PROJECT,
                credentials=credentials)
    client = CogniteClient(client_config)
    return client
