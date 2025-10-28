from pandas import DataFrame

from mdclass.models.base import BaseModel


def hyperparams(model: BaseModel) -> DataFrame:
    params = model.get_params()
    data = {'param_name': [], 'param_value': []}

    for name, value in params.items():
        data['param_name'].append(name)
        data['param_value'].append(value)

    df = DataFrame(data)

    return df


def feature_importances(model: BaseModel) -> DataFrame:
    features = model.feature_names_in_
    importances = model.feature_importances_

    data = {'feature_name': [], 'feature_importance': []}

    for name, importance in zip(features, importances):
        data['feature_name'].append(name)
        data['feature_importance'].append(importance)

    df = DataFrame(data)

    return df
