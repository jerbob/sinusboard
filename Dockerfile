FROM python:3.9-slim

ARG BUILD_DEPS="build-essential curl"

RUN set -ex \
  && apt-get update && apt-get -y --no-install-recommends install $BUILD_DEPS \
  && rm -rf /var/lib/apt/lists/* \
  && curl -sSL "https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py" | POETRY_PREVIEW=1 python \
  && . $HOME/.poetry/env \
  && poetry config virtualenvs.create false

COPY poetry.lock pyproject.toml /app/
WORKDIR /app/

ENV PYTHONUNBUFFERED=1 \
  PIP_NO_CACHE_DIR=off \
  PYTHONPYCACHEPREFIX=/tmp

RUN poetry install --no-root --no-interaction --no-dev \
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false $BUILD_DEPS

COPY . /app/

EXPOSE 8000

CMD ["gunicorn", "--workers", "12", "--bind", "0.0.0.0:8000", "sinusboard.server:app"]
