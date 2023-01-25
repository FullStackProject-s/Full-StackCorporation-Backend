# pull official base image
FROM python:3.10

# set work directory
WORKDIR /backend

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PROD 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY ./src ./src

# create dirs for logs
RUN mkdir logs logs/apps

# collect static files
RUN python src/manage.py collectstatic --noinput
