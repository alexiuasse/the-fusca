FROM python:3.7.4-alpine3.10

ADD backend/Pipfile /app/Pipfile
ADD backend/Pipfile.lock /app/Pipfile.lock

RUN set -ex \
    && apk add --no-cache --virtual postgresql-dev build-base \
    && /env/bin/pip install --upgrade pip \
    && /env/bin/pip install --user pipenv \
    && pipenv install

# COPY . /code/

ADD backend /app
WORKDIR /app

EXPOSE 8000

CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "app.wsgi"]