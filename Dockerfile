FROM python:3.11.9-alpine3.18

ENV PYTHONFAULTHANDLER=1 \
    PYTHONHASHSEED=random \
    PYTHONUNBUFFERED=1

ENV PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_CACHE_DIR='/var/cache/pypoetry' \
    POETRY_HOME='/usr/local' \
    POETRY_VERSION=1.8.2

RUN pip install poetry==1.8.2

WORKDIR /app
COPY pyproject.toml poetry.lock /app/

RUN poetry install --only=main --no-interaction --no-ansi

COPY ./ ./

CMD ["gunicorn", "joinup.wsgi:application", "--bind", "0.0.0.0:8000"]
