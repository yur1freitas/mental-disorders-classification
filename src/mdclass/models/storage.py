import joblib

from pathlib import Path

from mdclass.utils.path import ensure_directory
from mdclass.models.base import BaseModel
from mdclass import config

_MODELS_PATH = Path(config.models.root)


def save(
    model: BaseModel,
    filename: str = config.models.default,
) -> None:
    output_path = _MODELS_PATH / filename
    ensure_directory(output_path)

    joblib.dump(model, output_path, 1)


def load(filename: str = config.models.default) -> BaseModel:
    input_path = _MODELS_PATH / filename

    return joblib.load(input_path)
