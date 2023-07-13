import os
from dotenv import load_dotenv


__ENV_FILES = {"dev": ".env.dev", "prod": "env.prod"}


# loads env variables based on current ENV
def config_env():
    file_path = os.path.dirname(os.path.abspath(__file__))
    env_file = __ENV_FILES[os.environ.get("ENV")]
    load_dotenv(os.path.join(file_path, env_file))