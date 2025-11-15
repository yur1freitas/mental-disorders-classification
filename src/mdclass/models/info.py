from pandas import DataFrame

from mdclass.models.base import BaseModel


def hyperparams(estimator: BaseModel) -> DataFrame:
    """Função que extrai os parâmetros utilizados para treinar o modelo

    Args:
        estimator (BaseModel): Modelo ou estimador que deseja extrair essa informação

    Returns:
        DataFrame: Retorna uma DataFrame com os nomes dos parâmetros e seus respectivos valores
    """
    params = estimator.get_params()
    data = {'param_name': [], 'param_value': []}

    for name, value in params.items():
        data['param_name'].append(name)
        data['param_value'].append(value)

    df = DataFrame(data)

    return df


def feature_importances(estimator: BaseModel) -> DataFrame:
    """Função que permite extrair a 'importância' das features utilizadas para treinar o modelo

    Args:
        estimator (BaseModel): Modelo ou estimador que deseja extrair essa informação

    Returns:
        DataFrame: Retorna um DataFrame com os nomes das features com suas respectivas 'importâncias'
    """
    features = estimator.feature_names_in_
    importances = estimator.feature_importances_

    data = {
        'feature_name': features,
        'feature_importance': importances,
    }

    df = DataFrame(data)

    return df
