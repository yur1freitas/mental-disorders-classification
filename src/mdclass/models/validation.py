from collections.abc import Sequence
from dataclasses import dataclass

from numpy.typing import NDArray
from numpy import floating

from pandas import DataFrame, Series

from sklearn.model_selection import KFold, StratifiedKFold, cross_val_score

from mdclass.models.base import BaseModel
from mdclass.env import SEED

type CrossValidator = KFold | StratifiedKFold


def create_cv(
    name: str,
    *,
    n_splits: int = 5,
    shuffle: bool = True,
    random_state: int | None = SEED,
) -> CrossValidator:
    """Método responsável por instanciar o método de validação cruzada

    Args:
        name (str): Nome do método
        n_splits (int | None, optional): Quantidade de subgrupos que o conjunto de dados deve ser divido. Valor Padrão 5.
        shuffle (bool | None, optional): Propriedade que define se deve embaralhar os dados. Valor Padrão True.
        random_state (int | None, optional): Valor aleatório que controla o embaralhamento dos dados. Valor Padrão é a variável global 'SEED'.

    Returns:
        CrossValidator: Retorna o método de validação cruzada instanciado
    """

    match name:
        case 'stratified-kfold':
            return StratifiedKFold(
                n_splits=n_splits, shuffle=shuffle, random_state=random_state
            )
        case _:
            return KFold(
                n_splits=n_splits, shuffle=shuffle, random_state=random_state
            )


@dataclass
class CrossValOutput:
    raw: Sequence[float]
    scores: Series


def cross_val(
    estimator: BaseModel,
    X: DataFrame,
    y: Series,
    *,
    cv_type: str = 'kfold',
    scoring: str | None = None,
    n_splits: int | None = 5,
    shuffle: bool | None = True,
    random_state: int | None = SEED,
) -> CrossValOutput:
    """Função por aplicar validação cruzada em um modelo / estimador

    Args:
        estimator (BaseModel): Modelo ou estimador que deseja validar
        X (DataFrame): Features do dataset
        y (Series): Target do dataset
        cv_type (str, optional): Tipo de técnica de validação cruzada. Valor Padrão 'kfold'.
        scoring (str | None, optional): Tipo de método para pontuação do modelo. Valor Padrão None.
        shuffle (bool | None, optional): Propriedade que define se deve embaralhar os dados. Valor Padrão True.
        n_splits (int | None, optional): Quantidade de subgrupos que o conjunto de dados deve ser divido. Valor Padrão 5.
        random_state (int | None, optional): Valor aleatório que controla o embaralhamento dos dados. Valor Padrão é a variável global 'SEED'.

    Returns:
        CrossValOutput: Retorna uma saída contendo as pontuações ganhas pelo modelo
    """

    cv = create_cv(
        cv_type, n_splits=n_splits, shuffle=shuffle, random_state=random_state
    )

    scores: NDArray[floating] = cross_val_score(
        estimator,
        X,
        y,
        cv=cv,
        scoring=scoring,
        n_jobs=-1,
    )

    return CrossValOutput(
        raw=scores,
        scores=Series(scores),
    )
