FROM python:3.12.1-slim-bullseye

COPY ./ /app

WORKDIR /app

RUN apt-get update \
  && apt-get upgrade -y \
  && apt-get install wget gcc build-essential locales libreoffice libreoffice-base libreoffice-l10n-ja fonts-noto-cjk poppler-utils -y \
  && pip install -U pip \
  && pip install poetry \
  && poetry run pip install -U pip setuptools \
  && poetry install \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*


ENV PYTHONPATH=/app
ENV LANG ja_JP.UTF-8

RUN chmod +x /app/start.sh

# CMD [ "/app/start.sh" ]
# CMD [ "poetry", "run", "python", "main.py" ]

