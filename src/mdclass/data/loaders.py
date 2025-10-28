from pandas import DataFrame, read_csv
from pathlib import Path

from mdclass.utils.path import ensure_directory
from mdclass import config


_RAW_DATASETS_PATH = Path(config.datasets.root, config.datasets.raw)
_PROCESSED_DATASETS_PATH = Path(config.datasets.root, config.datasets.processed)


def load_raw_dataset(filepath: str = config.datasets.default) -> DataFrame:
    path = _RAW_DATASETS_PATH / filepath

    return read_csv(path)


def save_processed_dataset(
    dataset: DataFrame,
    filepath: str = config.datasets.default,
) -> None:
    path = _PROCESSED_DATASETS_PATH / filepath
    ensure_directory(path)

    dataset.to_csv(path, index=False)


def load_processed_dataset(
    filepath: str = config.datasets.default,
) -> DataFrame:
    path = _PROCESSED_DATASETS_PATH / filepath
    return read_csv(path)
