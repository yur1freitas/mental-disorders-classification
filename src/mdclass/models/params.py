from dataclasses import dataclass
from typing import cast

from pandas import DataFrame, Series

from sklearn.model_selection import GridSearchCV

from mdclass.models.validation import create_cv
from mdclass.models.base import BaseModel
from mdclass.env import SEED

type Params = dict[str, float | int | bool | str]

type ParamGrid = dict[str, list[float | int | bool | str]]


@dataclass
class SearchBestModelOutput:
    score: float
    model: BaseModel
    params: Params


def search_best_model(
    estimator_cls: type[BaseModel],
    X: DataFrame,
    y: Series,
    *,
    param_grid: ParamGrid | None = None,
    n_splits: int = 5,
    scoring: str = 'accuracy',
    cv_type: str = 'stratified-kfold',
    random_state: int | None = SEED,
) -> SearchBestModelOutput:
    estimator = estimator_cls(random_state=random_state)

    cv = create_cv(
        cv_type,
        n_splits=n_splits,
        shuffle=True,
        random_state=SEED,
    )

    grid = GridSearchCV(
        param_grid=param_grid,
        estimator=estimator,
        scoring=scoring,
        cv=cv,
        n_jobs=-1,
    )

    grid.fit(X, y)

    score = grid.best_score_
    model = grid.best_estimator_
    params = cast(Params, grid.best_params_)

    return SearchBestModelOutput(
        score=score,
        model=model,
        params=params,
    )
