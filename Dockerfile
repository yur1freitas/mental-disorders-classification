# -------------------------------------------------
#  Stage 1 – Base
# -------------------------------------------------
FROM python:3.14.0-slim-trixie AS base

# -------------------------------------------------
#  Stage 2 – Build
# -------------------------------------------------
FROM base AS build

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir uv && \ 
    uv venv ./venv/ && \
    . ./venv/bin/activate && \
    uv sync --no-dev && \
    uv build -o ./build/

# -------------------------------------------------
#  Stage 3 – Istall
# -------------------------------------------------
FROM base AS install

WORKDIR /app

COPY --from=build /app/build/*.whl ./build/

RUN python -m venv ./venv/ && \
    . ./venv/bin/activate && \
    pip install --no-cache-dir "$(ls ./build/*.whl | head -n 1)"

# -------------------------------------------------
#  Stage 4 – Runtime
# -------------------------------------------------
FROM base AS run

WORKDIR /app

COPY --from=install /app/venv/ ./venv/
RUN . ./venv/bin/activate

COPY models/ ./models/
COPY data/ ./data/
COPY config.toml .

EXPOSE 5000

RUN useradd --create-home nonroot && \
    chown -R nonroot:nonroot /app

USER nonroot

ENTRYPOINT ["/app/venv/bin/gunicorn", "-b", "0.0.0.0:5000", "mdclass:app"]