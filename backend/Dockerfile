
# Pull the official latest python docker image
FROM python:3.9.4-slim

# Set work directory
WORKDIR /app

# set env variable 
# PYTHONDONTWRITEBYTECODE =)> Prevents Python from writing pyc files to disc 
ENV PYTHONDONTWRITEBYTECODE 1
# PYTHONUNBUFFERED => Prevents Python from buffering stdout and stderr
ENV PYTHONUNBUFFERED 1

# Copy requirement file and install dependencies from it
COPY requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .
