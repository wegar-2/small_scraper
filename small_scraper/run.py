import os

print("Hello world! ")

print("trying to load defined environment variable...")
my_env = os.environ["TEST_ENV_VAR"]
print("my_env: ", my_env)

