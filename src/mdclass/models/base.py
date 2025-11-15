from typing import Protocol, Self

from pandas import DataFrame, Series


class BaseModel(Protocol):
    """
    Classe abstrata usada apenas para definir
    um tipo genérico de modelo para ser usado
    em parâmetros e variávels
    """

    feature_names_in_: list[str]
    feature_importances_: list[float]

    def __init__(self, random_state: int | None = None) -> None:
        super().__init__()

    def get_params(self) -> dict[str, str | float]: ...

    def fit(
        self,
        X: DataFrame,
        y: Series,
        sample_weight: list[float | int | bool] | None = None,
        check_input: bool = True,
    ) -> Self: ...

    def predict(self, X: DataFrame) -> list[tuple[int, int] | float]: ...
