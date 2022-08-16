import os
import numpy as np
import pandas as pd
from string import ascii_lowercase
from google.oauth2 import service_account


print("Hello world! ")
print("trying to load defined environment variable...")
my_env = os.environ["TEST_ENV_VAR"]
print("my_env: ", my_env)


print("creating data table...")
df = pd.DataFrame(
    data={
        "categ_A": np.random.choice(list(ascii_lowercase), replace=True, size=100),
        "var_X": np.random.randn(100)
    }
)


print("creating data table...")
info = os.environ["MY_SECRET_KEY"]
sa_credentials = service_account.Credentials.from_service_account_info(info)

print("uploading data table...")
df.to_gbq(
    destination_table="my_dataset.my_table2",
    project_id="default-359215",
    credentials=sa_credentials
)
