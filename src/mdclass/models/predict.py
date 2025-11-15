import pandas as pd

from dataclasses import asdict, dataclass

from mdclass.models.base import BaseModel


_CLASSES = (
    'Bipolaridade Tipo-1',
    'Bipolaridade Tipo-2',
    'Depressão',
    'Nada',
)


@dataclass
class PredictInput:
    mood_swing: bool = False
    suicidal_thoughts: bool = False
    anorxia: bool = False
    authority_respect: bool = False
    try_explanation: bool = False
    aggressive_response: bool = False
    ignore_and_move_on: bool = False
    nervous_break_down: bool = False
    admit_mistakes: bool = False
    overthinking: bool = False
    sexual_activity: float = 0
    concentration: float = 0
    optimisim: float = 0
    sadness: str = 'seldom'
    euphoric: str = 'seldom'
    exhausted: str = 'seldom'
    sleep_disorder: str = 'seldom'


@dataclass
class PredictOutput:
    value: int
    label: str
    params: PredictInput


def predict(
    model: BaseModel,
    params: PredictInput,
) -> PredictOutput:
    df = pd.DataFrame([asdict(params)])

    # -------------------------------------------------
    # Definindo as categorias disponíveis
    # -------------------------------------------------

    categories = ('sometimes', 'most_often', 'usually', 'seldom')
    dtype = pd.CategoricalDtype(categories=categories)

    # -------------------------------------------------
    # Aplicando Hot Enconding
    # -------------------------------------------------

    dummy_cols = ['sadness', 'euphoric', 'exhausted', 'sleep_disorder']

    df[dummy_cols] = df[dummy_cols].astype(dtype)
    df = pd.get_dummies(df, columns=dummy_cols, drop_first=False)

    # -------------------------------------------------
    # Reorganizando o DataFrame com base na ordem dos parâmetros treinados
    # -------------------------------------------------

    df = df.reindex(model.feature_names_in_, axis=1)

    # -------------------------------------------------
    # Predição e rótulo correspondente
    # -------------------------------------------------

    pred = model.predict(df)[0]

    value = int(pred)
    label = _CLASSES[value]

    return PredictOutput(
        value=value,
        label=label,
        params=params,
    )
