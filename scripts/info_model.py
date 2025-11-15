from mdclass.models.info import hyperparams, feature_importances
from mdclass.models import storage


def main() -> None:
    model = storage.load()

    print('- - - Hyper Parâmetros - - -')
    print(hyperparams(model))

    print('- - - Importância dos Parâmetros - - -')
    print(feature_importances(model))


if __name__ == '__main__':
    main()
