import logging.handlers
import os
import sys
from pathlib import Path
from typing import Any, Callable, List, Optional, Union


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


def setup_logger(logger_name: str = "server", level: int = logging.DEBUG) -> None:
    """Setup basic logging config"""
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
