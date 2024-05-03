FROM python:3.10-bookworm

ENV PYTHONFAULTHANDLER=1 \
  PYTHONUNBUFFERED=1 \
  PYTHONHASHSEED=random \
  POETRY_NO_INTERACTION=1 \
  POETRY_VIRTUALENVS_CREATE=false \
  POETRY_HOME='/usr/local/' \
  PATH="${PATH}:${POETRY_HOME}"


RUN apt-get update && apt-get install libpq-dev python3-dev default-libmysqlclient-dev build-essential curl -y --no-install-recommends\
    && curl -sSL https://install.python-poetry.org | python3 -
WORKDIR /app
COPY . /app/
RUN python3 -m pip install -U tox



CMD ["tox"]
