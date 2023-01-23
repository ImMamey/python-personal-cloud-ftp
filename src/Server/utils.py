import logging.handlers
import os
import socket
import sys
from pathlib import Path
from typing import Union


def get_ip() -> str:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))

    local_ip = s.getsockname()[0]
    print(local_ip)
    s.close()
    return local_ip


def data_path(path: Union[Path, str], is_folder: bool = False) -> Path:
    """Return a valid local data path, docker-aware"""
    if os.environ.get("RUNNING_IN_DOCKER", False):
        _path = Path("/data") / path
    else:
        _path = Path.cwd() / "data" / path

    folder = _path
    if not is_folder:
        folder = _path.parent

    # Create folders if necessary
    if not folder.exists():
        os.makedirs(folder, exist_ok=True)

    return _path


def user_dir(user_name: str) -> None:
    """Setup basic dirs for each user"""
    data_path(f"storage/{user_name}", is_folder=True)


def setup_logger(logger_name: str = "server", level: int = logging.DEBUG) -> None:
    """Setup basic logging config"""
    storage_folder = data_path("storage", is_folder=True)
    log_folder = data_path("logs", is_folder=True)

    fmt = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s", "%Y-%m-%d %H:%M:%S"
    )

    hldr = logging.handlers.TimedRotatingFileHandler(
        str(log_folder / "Server.log"), when="W0", encoding="utf-8", backupCount=16
    )
    hldr.setFormatter(fmt)
    hldr.setLevel(logging.DEBUG)

    stream = logging.StreamHandler(sys.stdout)
    stream.setFormatter(fmt)
    stream.setLevel(level)

    if logger_name != "server":
        bot_log = logging.getLogger("server")
        bot_log.addHandler(hldr)
        bot_log.setLevel(logging.DEBUG)
        bot_log.addHandler(stream)

    log = logging.getLogger(logger_name)
    log.addHandler(hldr)
    log.setLevel(logging.DEBUG)
    log.addHandler(stream)
