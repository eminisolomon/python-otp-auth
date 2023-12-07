FROM python:3.8-alpine

# Install system dependencies
RUN apk add --no-cache \
    gcc \
    python3-dev \
    build-base \
    libffi-dev \
    libxml2-dev \
    musl-dev \
    libxslt-dev \
    curl

# Copy only the necessary files
COPY ./pyproject.toml /
COPY ./poetry.lock /

# Install Poetry
RUN pip install -U pip poetry

# Install project dependencies
RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

# Copy the rest of the application code
COPY . /src
WORKDIR /src

# Expose the port
EXPOSE 5000

# Set up entry point
COPY start.sh /src/start.sh
RUN chmod +x /src/start.sh

# Specify the command to run on container start
CMD ["/src/start.sh"]
