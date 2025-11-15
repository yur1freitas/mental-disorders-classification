import os

from pathlib import Path


def ensure_directory(path: Path) -> None:
    """Garanta que os diretórios do caminho especificado existam

    Args:
        path (Path): Um caminho para um diretório ou arquivo
    """
    if not os.path.exists(path.parent):
        os.makedirs(path.parent)
