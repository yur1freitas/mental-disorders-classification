from typing import cast

from pandas import DataFrame, Series
from sklearn.model_selection import train_test_split

from mdclass.models.base import BaseModel
from mdclass.models import storage
from mdclass.env import SEED


def feature_target_split(
    dataset: DataFrame,
    y_column: str,
) -> tuple[DataFrame, Series]:
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
    model: BaseModel,
    X: DataFrame,
    y: Series,
    *,
    filename: str,
) -> None:
    storage.save(model=model.fit(X, y), filename=filename)
