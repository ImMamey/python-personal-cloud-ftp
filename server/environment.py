from typing import Optional

from dotenv import load_dotenv
from pydantic import BaseSettings
import os
import sys

# load .env in dev enviroment
extDataDir = os.getcwd()
if getattr(sys, "frozen", False):
    extDataDir = sys._MEIPASS
load_dotenv(dotenv_path=os.path.join(extDataDir, ".env"))


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
