from typing import Any

import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier

from mdclass.data.loaders import load_processed_dataset
from mdclass.models import storage
from mdclass.models.params import (
    SearchBestModelOutput,
    search_best_model,
)
from mdclass.models.training import feature_target_split


def create_models_cfg():
    return {
        # 'DecisionTreeClassifier': {
        #     'estimator': DecisionTreeClassifier,
        #     'param_grid': {
        #         'max_depth': [3, 6, 7, 9, 10, None],
        #         'criterion': ['gini', 'entropy', 'log_loss'],
        #     },
        # },
        'RandomForestClassifier': {
            'estimator': RandomForestClassifier,
            'param_grid': {
                'max_depth': [3, 4, 6, 9],
                'n_estimators': [50, 100, 200],
                'criterion': ['entropy'],
            },
        },
        'GradientBoostingClassifier': {
            'estimator': GradientBoostingClassifier,
            'param_grid': {
                'n_estimators': [50, 100, 200],
                'learning_rate': [0.01, 0.05, 0.1],
            },
        },
    }


def main() -> None:
    dataset = load_processed_dataset()
    X, y = feature_target_split(dataset, y_column='expert_diagnose')

    best_global: Any = None  # pyright: ignore[reportExplicitAny]
    n_iterations = 100

    models_cfg = create_models_cfg()

    for _ in range(n_iterations):
        iteration_results = []

        for name, cfg in models_cfg.items():
            cls = cfg['estimator']
            param_grid = cfg['param_grid']

            search: SearchBestModelOutput = search_best_model(
                cls,
                X,
                y,
                param_grid=param_grid,
                cv_type='kfold',
                scoring='accuracy',
            )

            model = search.model
            params = search.params

            iteration_results.append(
                {
                    'name': name,
                    'model': model,
                    'params': params,
                    'score': search.score,
                }
            )

        df_iter = pd.DataFrame(iteration_results)

        best_current = df_iter.sort_values(
            by=['score'],
            ascending=[False],
        ).iloc[0]

        if best_global is None or best_current['score'] < best_global['score']:
            best_global = best_current

    storage.save(best_global['model'])

    print(
        f'Melhor modelo: {best_global["name"]} com SCORE={best_global["score"]}'
    )


if __name__ == '__main__':
    main()
