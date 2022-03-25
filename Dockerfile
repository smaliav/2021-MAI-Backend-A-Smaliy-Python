FROM python:3.8-slim-buster

ADD . /app
WORKDIR /app
RUN apt-get update \
    && apt-get -y install libpq-dev gcc
RUN pip install -r requirements.txt

ENTRYPOINT ["python", "thatcar/manage.py", "runserver"]
