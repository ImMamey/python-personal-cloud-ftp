from typing import Optional

from dotenv import load_dotenv
from pydantic import BaseSettings

# load .env in dev enviroment
load_dotenv()


class Environment(BaseSettings):
    """Loads the contents of a private .env file to the system
    This .env should have the default password and username for the FTP server.
    It's highly recommended to add the .env to the .gitignore file for security reasons.
    """
    USER: str
    PASSWORD: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


env = Environment()
