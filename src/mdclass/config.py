import tomllib as toml

from dataclasses import dataclass
from os import getenv

_DEFAULT_CONFIG_FILE = 'config.toml'


@dataclass
class DatasetsConfig:
    """
    Classe de dados que representa a configuração 'datasets' em 'config.toml'
    """

    root: str
    raw: str
    processed: str
    default: str


@dataclass
class ModelsConfig:
    """
    Classe de dados que representa a configuração 'models' em 'config.toml'
    """

    root: str
    default: str


@dataclass
class Config:
    """
    Classe de dados que representa 'config.toml'
    """

    models: ModelsConfig
    datasets: DatasetsConfig


def load() -> Config:
    """Função responsável por ler a configuração na raiz do projeto (config.toml)

    Returns:
        Config: Retorna a configuração
    """

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
