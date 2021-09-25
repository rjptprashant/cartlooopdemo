# Pull base image
FROM python:3.9-slim

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


# Set work directory
WORKDIR /app

# Install dependencies
RUN apt-get update && apt-get install -y binutils libproj-dev gdal-bin libgdal-dev poppler-utils

# Copy project requirements file
COPY requirements.txt /app/

# Run install lib command
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . /app/