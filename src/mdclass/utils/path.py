import os

from pathlib import Path


def ensure_directory(path: Path) -> None:
    if not os.path.exists(path.parent):
        os.makedirs(path.parent)
