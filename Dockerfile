FROM python:3.6
ENV PYTHONUNBUFFERED 1
WORKDIR /usr/src/survaider_backend

COPY ./ /usr/src/survaider_backend

RUN pip install -r requirements.txt
