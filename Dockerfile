FROM python:3.10-buster

WORKDIR /app

ENV DJANGO_SETTINGS_MODULE = 'config.settings'

ENV PYTHONUNBUFFERED=1

# Install dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    python3-dev \
    python3-pip \
    python3-setuptools \
    python3-wheel \
    python3-venv \
    && rm -rf /var/lib/apt/lists/*

RUN python3 -m pip install --upgrade pip

RUN pip install poetry

COPY pyproject.toml ./

COPY poetry.lock ./

RUN poetry install

COPY . .

RUN poetry add django

CMD ["poetry","run","make","start"]
