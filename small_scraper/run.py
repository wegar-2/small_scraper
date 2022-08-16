import os
import numpy as np
import pandas as pd
from string import ascii_lowercase
from google.oauth2 import service_account
import json

print("Hello world! ")
print("trying to load defined environment variable...")
my_env = os.environ["TEST_ENV_VAR"]
print("my_env: ", my_env)


print("loading environment vars needed to connect to GCP...")
env_type = os.environ["ENV_TYPE"]
env_project_id = os.environ["ENV_PROJECT_ID"]
env_private_key_id = os.environ["ENV_PRIVATE_KEY_ID"]
env_private_key = os.environ["ENV_PRIVATE_KEY"]
env_client_email = os.environ["ENV_CLIENT_EMAIL"]
env_client_id = os.environ["ENV_CLIENT_ID"]
env_auth_uri = os.environ["ENV_AUTH_URI"]
env_token_uri = os.environ["ENV_TOKEN_URI"]
env_auth_provider = os.environ["ENV_AUTH_PROVIDER"]
env_client_cert = os.environ["ENV_CLIENT_CERT"]


my_dict = {
  "type": env_type,
  "project_id": env_project_id,
  "private_key_id": env_private_key_id,
  "private_key": env_private_key,
  "client_email": env_client_email,
  "client_id": env_client_id,
  "auth_uri": env_auth_uri,
  "token_uri": env_token_uri,
  "auth_provider_x509_cert_url": env_auth_provider,
  "client_x509_cert_url": env_client_cert
}

print("creating data table...")
df = pd.DataFrame(
    data={
        "categ_A": np.random.choice(list(ascii_lowercase), replace=True, size=100),
        "var_X": np.random.randn(100)
    }
)


print("creating credentials...")
sa_credentials = service_account.Credentials.from_service_account_info(my_dict)

print("uploading data table...")
df.to_gbq(
    destination_table="my_dataset.my_table2",
    project_id="default-359215",
    credentials=sa_credentials
)

