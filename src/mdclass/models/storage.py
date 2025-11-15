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
    """Função responsável por salvar o modelo treinado no diretório configurado em 'config.toml'

    Args:
        model (BaseModel): Modelo ou estimador que deseja salvar
        filename (str, optional): Nome do arquivo que deseja salvar. Valor padrão é o 'models.default' em 'config.toml'.
    """

    output_path = _MODELS_PATH / filename
    ensure_directory(output_path)

    joblib.dump(model, output_path, 1)


def load(filename: str = config.models.default) -> BaseModel:
    """Função responsável por carregar o modelo treinando a partir do diretório configurado em 'config.toml'

    Args:
        filename (str, optional):  Nome do arquivo que deseja carregar. Valor padrão é o 'models.default' em 'config.toml'.

    Returns:
        BaseModel: Retorna o modelo carregado
    """

    input_path = _MODELS_PATH / filename

    return joblib.load(input_path)
