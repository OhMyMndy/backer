FROM python:3.9.16-buster as builder

ENV MODEL_PATH /model
ARG MODEL=5stems
RUN mkdir -p /model/$MODEL \
    && wget -O /tmp/$MODEL.tar.gz https://github.com/deezer/spleeter/releases/download/v1.4.0/$MODEL.tar.gz \
    && tar -xvzf /tmp/$MODEL.tar.gz -C /model/$MODEL/ \
    && touch /model/$MODEL/.probe

RUN apt-get update \
  && apt-get install libc++-dev libblas-dev python3-dev ffmpeg libsndfile1 -y

ARG CACHEBUST
COPY requirements.txt /app/requirements.txt

#RUN python3 -m venv --copies /app/.venv
RUN pip3 install -r /app/requirements.txt


WORKDIR /app

COPY main.py /app/main.py
COPY entrypoint.sh /app/entrypoint.sh

FROM builder as final

ENTRYPOINT ["/app/entrypoint.sh"]