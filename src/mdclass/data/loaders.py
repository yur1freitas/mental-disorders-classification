from pandas import DataFrame, read_csv
from pathlib import Path

from mdclass.utils.path import ensure_directory
from mdclass import config


_RAW_DATASETS_PATH = Path(config.datasets.root, config.datasets.raw)
_PROCESSED_DATASETS_PATH = Path(config.datasets.root, config.datasets.processed)


def load_raw_dataset(filepath: str = config.datasets.default) -> DataFrame:
    """Função responsável por ler os datasets originais sem processamento. Suporte apenas para CSV

    Args:
        filepath (str, optional): Caminho para o dataset, relativo a raiz definida em 'config.toml'. Valor padrão é o 'datasets.default' em 'config.toml'.

    Returns:
        DataFrame: Retorna o dataset carregado
    """

    path = _RAW_DATASETS_PATH / filepath

    return read_csv(path)


def save_processed_dataset(
    dataset: DataFrame,
    filepath: str = config.datasets.default,
) -> None:
    """Função responsável por salvar os datasets processados. Suporte apenas para CSV

    Args:
        dataset (DataFrame): Dataset que deseja salvar
        filepath (str, optional): Caminho onde deseja salvar o dataset, relativo a raiz definida em 'config.toml'. Valor padrão é o 'datasets.default' em 'config.toml'.
    """

    path = _PROCESSED_DATASETS_PATH / filepath
    ensure_directory(path)

    dataset.to_csv(path, index=False)


def load_processed_dataset(
    filepath: str = config.datasets.default,
) -> DataFrame:
    """Função responsável por lear os datasets processados. Suporte apenas para CSV

    Args:
        filepath (str, optional): Caminho para o dataset, relativo a raiz definida em 'config.toml'. Valor padrão é o 'datasets.default' em 'config.toml'.

    Returns:
        DataFrame: Retorna o dataset carregado
    """

    path = _PROCESSED_DATASETS_PATH / filepath
    return read_csv(path)
