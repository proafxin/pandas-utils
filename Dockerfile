FROM python:3.10-bookworm

ENV PYTHONUNBUFFERED=1
ENV PYTHONHASHSEED=random
ENV POETRY_NO_INTERACTION=1
ENV POETRY_VIRTUALENVS_CREATE=false
ENV POETRY_HOME='/usr/local/'
ENV PATH="${PATH}:${POETRY_HOME}"


RUN apt-get update && apt-get install libpq-dev python3-dev default-libmysqlclient-dev build-essential curl -y --no-install-recommends\
    && curl -sSL https://install.python-poetry.org | python3 -
WORKDIR /app
COPY . /app/
RUN python3 -m pip install -U tox



CMD ["tox"]
