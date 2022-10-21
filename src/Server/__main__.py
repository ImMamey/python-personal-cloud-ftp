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
def main(server_ip: str)-> None:
    # Instantiate a dummy authorizer for managing 'virtual' users
    authorizer = DummyAuthorizer()

    # Define a new user having full r/w permissions and a read-only
    # anonymous user
    authorizer.add_user( env.USER, env.PASSWORD, '.', perm='elradfmwMT')
    # authorizer.add_anonymous(os.getcwd())

    # Instantiate FTP handler class
    handler = FTPHandler
    handler.authorizer = authorizer

    # Define a customized banner (string returned when client connects)
    handler.banner = "pyftpdlib based ftpd ready."

    # Specify a masquerade address and the range of ports to use for
    # passive connections.  Decomment in case you're behind a NAT.
    # handler.masquerade_address = '151.25.42.11'
    # handler.passive_ports = range(60000, 65535)
    #logging.basicConfig(filename='/var/log/pyftpd.log', level=logging.INFO)
    # Instantiate FTP server class and listen on 0.0.0.0:2121
    address = (server_ip, 21)
    server = FTPServer(address, handler)

    # set a limit for connections
    server.max_cons = 256
    server.max_cons_per_ip = 5

    # start ftp server
    server.serve_forever()
def storage_path()->None:
    if not os.path.exists("data\storage"):
        print(f"Relative path `data\stprage` does not exist")
        LOG.info(f"FAILIURE: relative path `data\stprage` wasnt created by the logger")
    else:
        print("Path data\storage is created, succesfully accessed")

#TODO: Divide the and above code to an separate "Service.py" class.
if __name__ == '__main__':
    server_ip = ip.ip.get_ip()
    try:
        setup_logger(logger_name="server")
        storage_path()
        print(f"FTP server is running on the ip: {server_ip}")
        print(f"Running on: {platform.system()} {platform.release()} ({os.name})")
        print("--------")
        LOG.info(f"Running on: {platform.system()} {platform.release()} ({os.name}) on the ip: {server_ip}")
    except Exception as e:
        exception = f"{type(e).__name__}: (e)"
        print(f"Failed to setup logger and/or ftp folder:\n {exception}")
    main(server_ip)
