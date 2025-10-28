from mdclass.data.loaders import save_processed_dataset
from mdclass.data.process import process_dataset


def main() -> None:
    dataset = process_dataset()
    save_processed_dataset(dataset)


if __name__ == '__main__':
    main()
