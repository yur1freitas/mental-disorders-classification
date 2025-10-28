from mdclass.data.loaders import load_processed_dataset
from mdclass.models import storage
from mdclass.models.training import feature_target_split
from mdclass.models.validation import cross_val


def main() -> None:
    model = storage.load()
    dataset = load_processed_dataset()

    X, y = feature_target_split(dataset, 'expert_diagnose')
    result = cross_val(model, X, y)

    print(f'Pontuação Média: {result.scores.mean()}')


if __name__ == '__main__':
    main()
