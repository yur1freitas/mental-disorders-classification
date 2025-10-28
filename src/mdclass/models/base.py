from typing import Protocol, Self

from pandas import DataFrame, Series


class BaseModel(Protocol):
    feature_names_in_: list[str]
    feature_importances_: list[float]

    def __init__(self, random_state: int | None = None) -> None:
        super().__init__()

    def fit(
        self,
        X: DataFrame,
        y: Series,
        sample_weight: list[float | int | bool] | None = None,
        check_input: bool = True,
    ) -> Self: ...

    def predict(self, X: DataFrame) -> list[tuple[int, int] | float]: ...

    def get_params(self) -> dict[str, str | float]: ...
