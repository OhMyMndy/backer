FROM python:3.10.11-buster

RUN apt-get update \
  && apt-get install libc++-dev libblas-dev -y

ARG CACHEBUST
COPY requirements.txt /app/requirements.txt

RUN python3 -m venv /app/.venv
RUN /app/.venv/bin/pip3 install -r /app/requirements.txt

WORKDIR /app

COPY main.py /app/main.py
COPY entrypoint.sh /app/entrypoint.sh


ENTRYPOINT ["/app/entrypoint.sh"]