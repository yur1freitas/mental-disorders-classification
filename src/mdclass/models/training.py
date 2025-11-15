from typing import cast

from sklearn.model_selection import train_test_split
from pandas import DataFrame, Series

from mdclass.models.base import BaseModel
from mdclass.models import storage
from mdclass.env import SEED


def feature_target_split(
    dataset: DataFrame,
    y_column: str,
) -> tuple[DataFrame, Series]:
    """Função responsável por separar o dataset da coluna que desejamos que o modelo ou estimador predite

    Args:
        dataset (DataFrame): DataSet que deseja aplicar a separação
        y_column (str): Nome da coluna alvo

    Returns:
        tuple[DataFrame, Series]: Retorna as features e o target
    """

    features = dataset.drop(columns=[y_column])
    target = cast(Series, dataset[y_column])

    return features, target


def train_val_split(
    X: DataFrame,
    y: Series,
    *,
    test_size: float | None = 0.25,
    train_size: float | None = None,
    random_state: int | None = SEED,
) -> tuple[DataFrame, DataFrame, Series, Series]:
    """Função responsável por separar o dataset em treino e teste

    Args:
        X (DataFrame): Features do dataset
        y (Series): Target do dataset
        test_size (float | None, optional): Tamanho do conjunto para teste em porcentagem. Valor Padrão 0.25.
        train_size (float | None, optional): Tamanho do conjunto para treino em porcentagem. Valo Padrão None.
        random_state (int | None, optional): Valor aleatório que controla o embaralhamento dos dados. Valor Padrão é a variável global 'SEED'.

    Returns:
        tuple[DataFrame, DataFrame, Series, Series]: Retorna o conjunto de treino e teste de X e y, respectivamente
    """

    X_train, X_val, y_train, y_val = train_test_split(
        X,
        y,
        shuffle=True,
        stratify=y,
        test_size=test_size,
        train_size=train_size,
        random_state=random_state,
    )

    return X_train, X_val, y_train, y_val


def fit_model(
    estimator: BaseModel,
    X: DataFrame,
    y: Series,
    *,
    filename: str,
) -> None:
    """Função responsável por treinar o modelo e o salvar

    Args:
        estimator (BaseModel): Modelo ou estimador que deseja treinar
        X (DataFrame): Features do dataset
        y (Series): Target do dataset
        filename (str): Nome do arquivo que deseja salvar
    """

    storage.save(model=estimator.fit(X, y), filename=filename)
