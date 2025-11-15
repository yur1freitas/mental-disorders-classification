import re

from collections.abc import Iterable
from functools import reduce
from typing import Callable

from pandas import DataFrame


def strip_str(df: DataFrame) -> DataFrame:
    """Remove espaços desnecessários dos valores textuais do DataFrame

    Args:
        df (DataFrame): DataFrame que deseja aplicar a transformação nos valores

    Returns:
        DataFrame: Retorna o DataFrame com os valores transformados
    """

    df_copy = df.copy(deep=True)

    df_obj = df_copy.select_dtypes('object')
    df_copy[df_obj.columns] = df_obj.map(str.strip)

    return df_copy


def to_snake_case(df: DataFrame) -> DataFrame:
    """Transforma os nomes das colunas para o formato snake_case

    Args:
        df (DataFrame): DataFrame que deseja aplicar a transformação nos nomes colunas

    Returns:
        DataFrame: DataFrame com os nomes das colunas transformados
    """

    df_copy = df.copy(deep=True)

    # Transformadores
    pipes: Iterable[Callable[[str], str]] = (
        # Remove espaços desnecessários
        str.strip,
        # Substitui todo espaço em branco e hífens por underline
        lambda x: re.sub(r'[\s\-]+', '_', x),
        # Substitui o '&' por underline
        lambda x: re.sub(r'&', 'and', x),
        # Transforma tudo em minúsculo
        str.lower,
    )

    def transform(value: str) -> str:
        return reduce(lambda x, pipe: pipe(x), pipes, value)

    df_copy.columns = df_copy.columns.map(transform)

    return df_copy
