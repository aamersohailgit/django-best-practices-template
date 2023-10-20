# Use the specified Python version
FROM python:3.12.0-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create and set the working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
        libsqlite3-dev \
    && rm -rf /var/lib/apt/lists/* \
    && pip install --upgrade pip

# Copy the Pipfile and install Python dependencies
COPY ./main/requirements.txt /app/
RUN pip install -r requirements.txt

# Copy the content of the local src directory to the working directory
COPY ./main /app/
