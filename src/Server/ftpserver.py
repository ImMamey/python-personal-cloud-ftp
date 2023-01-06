import os
import logging
import platform

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
from src.Server.utils import setup_logger
from environment import env
from pathlib import Path
import ip

LOG = logging.getLogger("server")

def main(server_ip: str, storage_path: str) -> None:

    authorizer = DummyAuthorizer()

    # TODO: The line bellow creates the users for our ftp server, if we want multiple users we would need to have more lines of these.
    authorizer.add_user(env.USER, env.PASSWORD, storage_path, perm="elradfmwMT")


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
    if not os.path.exists("data\storage"):
        print(f"Relative path `data\stprage` does not exist")
        LOG.info(f"FAILIURE: relative path `data\stprage` wasnt created by the logger")
    else:
        print("Path data\storage is created, succesfully accessed")
    return "data\storage"


# TODO: Divide the and above code to an separate "Service.py" class.
if __name__ == "__main__":
    server_ip = ip.ip.ip.get_ip()
    '''
    Setting up logs and making dirs for the working server
    '''
    try:
        setup_logger(logger_name="server")
        storage_path = storage_path()
        logging.basicConfig(filename='data/logs/pyftpd.log', level=logging.INFO)
        logging.basicConfig(level=logging.DEBUG)
        print(f"FTP server is running on the ip: {server_ip}")
        print(f"Running on: {platform.system()} {platform.release()} ({os.name})")
        print("--------")
        LOG.info(
            f"Running on: {platform.system()} {platform.release()} ({os.name}) on the ip: {server_ip}"
        )
    except Exception as e:
        exception = f"{type(e).__name__}: (e)"
        print(f"Failed to setup logger and/or ftp folder:\n {exception}")
        LOG.info(
            f"Failed to setup logger and/or ftp folder:\n {exception}"
        )

    main(server_ip, storage_path)


