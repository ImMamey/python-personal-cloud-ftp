import os
import logging
import platform
import sqlite3

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
from src.Server.utils import setup_logger, user_dir, get_ip
from environment import env

LOG = logging.getLogger("server")


def create_users_fromdb(autorizer) -> None:
    """
    Populates the ftp server with users and creates the necessary directories
    :return:
    """
    db = None
    try:
        db = sqlite3.connect("users.db")
    except Exception as e:
        print(e)

    # SQL commands and cursors
    cursor = db.cursor()
    command = "SELECT user, password FROM users"

    result = cursor.execute(command)

    for row_number, row_data in enumerate(result):
        user = row_data[0]
        password = row_data[1]
        try:
            user_dir(user)
            autorizer.add_user(user, password, f"data/storage/{user}", perm="elradfmw")
            LOG.info("Created user: %s with dir: /data/storage/%s", user, password)
        except (IOError, ValueError):
            LOG.exception("Failed to create directory for user: %s", user)


def refresh_users() -> None:
    authorizer = DummyAuthorizer()
    create_users_fromdb(authorizer)


def main(server_ip: str, path: str) -> None:
    authorizer = DummyAuthorizer()

    # TODO: The line below creates the users for our ftp server, if we want multiple users we would need to have more lines of these.
    authorizer.add_user(env.USER, env.PASSWORD, path, perm="elradfmwMT")
    create_users_fromdb(authorizer)

    handler = FTPHandler
    handler.authorizer = authorizer

    # Define a customized banner (string returned when client connects)
    handler.banner = "pyftpdlib based ftpd ready."

    address = (server_ip, 2121)
    server = FTPServer(address, handler)

    server.max_cons = 256
    server.max_cons_per_ip = 5

    server.serve_forever()


def storage_path() -> str:
    if not os.path.exists("data/storage"):
        print("Relative path `data/storage` does not exist")
        LOG.info("FAILURE: relative path `data/storage` wasn't created by the logger")
    else:
        print("Path data/storage is created, succesfully accessed")
    return "data/storage"


def run_server() -> None:
    """
    Setting up logs and making dirs for the working server
    """
    server_ip = get_ip()
    try:
        setup_logger(logger_name="server")
        _storage = storage_path()
        logging.basicConfig(filename='data/logs/pyftpd.log', level=logging.INFO)
        logging.basicConfig(level=logging.DEBUG)
        print(f"FTP server is running on the ip: {server_ip}")
        print(f"Running on: {platform.system()} {platform.release()} ({os.name})")
        print("--------")
        LOG.info(
            f"Running on: {platform.system()} {platform.release()} ({os.name}) on the ip: {server_ip}"
        )
        main(server_ip, _storage)
    except Exception as e:
        exception = f"{type(e).__name__}: (e)"
        print(f"Failed to setup logger and/or ftp folder:\n {exception}")
        LOG.info(
            f"Failed to setup logger and/or ftp folder:\n {exception}"
        )

