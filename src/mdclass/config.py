import tomllib as toml
from dataclasses import dataclass
from os import getenv

_DEFAULT_CONFIG_FILE = 'config.toml'


@dataclass
class DatasetsConfig:
    root: str
    raw: str
    processed: str
    default: str


@dataclass
class ModelsConfig:
    root: str
    default: str


@dataclass
class Config:
    models: ModelsConfig
    datasets: DatasetsConfig


def load() -> Config:
    filepath = getenv('CONFIG_PATH', default=_DEFAULT_CONFIG_FILE)

    with open(filepath, 'rb') as f:
        data = toml.load(f)

    models_config = ModelsConfig(**data['models'])
    datasets_config = DatasetsConfig(**data['datasets'])

    return Config(
        models=models_config,
        datasets=datasets_config,
    )


config = load()
models = config.models
datasets = config.datasets
