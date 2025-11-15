import pandas as pd

from sklearn.preprocessing import LabelEncoder

from mdclass.data.loaders import load_raw_dataset
from mdclass.utils import dataframe as dfutils


pd.set_option('future.no_silent_downcasting', True)


def _parse_scale(value: str) -> float:
    """Função responsável por converter os valores em escala do dataset em números

    Args:
        value (str): Valor em escala

    Returns:
        float: Retorna o valor numérico correspondente
    """

    try:
        left, right = value.lower().split('from')
        return float(left.strip()) / float(right.strip())
    except Exception:
        return float('nan')


def process_dataset() -> pd.DataFrame:
    """Função responsável por processar o dataset, convertendo todos os valores para números

    Returns:
        pd.DataFrame: Retorna o dataset processado
    """

    df = load_raw_dataset()

    # -------------------------------------------------
    # Removendo colunas desnecessárias
    # -------------------------------------------------

    df = df.drop(columns=['Patient Number'], errors='ignore')

    # -------------------------------------------------
    # Removendo espaços em brancos desnecessários
    # -------------------------------------------------

    df = dfutils.strip_str(df)

    # -------------------------------------------------
    # Convertendo colunas para binário
    # -------------------------------------------------

    binary_cols = [
        'Aggressive Response',
        'Nervous Break-down',
        'Authority Respect',
        'Suicidal thoughts',
        'Ignore & Move-On',
        'Try-Explanation',
        'Admit Mistakes',
        'Overthinking',
        'Mood Swing',
        'Anorxia',
    ]

    df[binary_cols] = df[binary_cols].replace({'YES': True, 'NO': False})

    # -------------------------------------------------
    # Aplicando Hot Enconding
    # -------------------------------------------------

    dummy_cols = ['Sadness', 'Euphoric', 'Exhausted', 'Sleep disorder']
    df = pd.get_dummies(df, columns=dummy_cols, drop_first=False)

    # -------------------------------------------------
    # Realizando parsing nas Escalas
    # -------------------------------------------------

    scale_cols = ['Sexual Activity', 'Concentration', 'Optimisim']
    for col in scale_cols:
        df[col] = df[col].map(_parse_scale)

    # -------------------------------------------------
    # Transformando as features target em valores numéricos
    # -------------------------------------------------

    target_col = 'Expert Diagnose'

    le = LabelEncoder()
    df[target_col] = le.fit_transform(df[target_col])

    # -------------------------------------------------
    # Convertendo os nomes das colunas para snake_case
    # -------------------------------------------------

    df = dfutils.to_snake_case(df)

    return df
