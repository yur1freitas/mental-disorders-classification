dev:
    uv run flask --app mdclass run

start: 
    uv run gunicorn mdclass:app

fmt:
    uv run dprint fmt && uv run ruff format

process-data:
    uv run -m scripts.process_dataset

train:
    uv run -m scripts.train_model

validate:
    uv run -m scripts.validate_model

build-model:
    MODE=production just process-dataset && just train-model

build-app:
    MODE=production uv build -o build

docs:
    uv run pdoc -d google mdclass -o docs/

preview-docs:
    uv run pdoc -h localhost -p 3000 mdclass