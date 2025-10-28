from collections.abc import Sequence
from dataclasses import dataclass

from numpy.typing import NDArray
from numpy import floating

from pandas import DataFrame, Series

from sklearn.model_selection import KFold, StratifiedKFold, cross_val_score
from sklearn.metrics import mean_squared_error

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
    shuffle: bool | None = True,
    n_splits: int | None = 5,
    random_state: int | None = SEED,
) -> CrossValOutput:
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


@dataclass
class MSEOutput:
    var: float
    mean: float
    scores: NDArray[floating]


def mse(
    estimator: BaseModel,
    X: DataFrame,
    y: Series,
    *,
    cv_type: str = 'kfold',
    shuffle: bool | None = True,
    n_splits: int | None = 5,
    random_state: int | None = SEED,
) -> MSEOutput:
    cv = create_cv(
        cv_type, n_splits=n_splits, shuffle=shuffle, random_state=random_state
    )

    scores: NDArray[floating] = cross_val_score(
        estimator,
        X,
        y,
        cv=cv,
        scoring='neg_mean_squared_error',
        n_jobs=-1,
    )

    return MSEOutput(
        scores=scores,
        var=scores.var(),
        mean=scores.mean(),
    )


def mse_val(
    estimator: BaseModel,
    X: DataFrame,
    y: Series,
) -> float:
    return mean_squared_error(y, estimator.predict(X))
