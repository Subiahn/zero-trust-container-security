FROM python:3.11-slim

WORKDIR /app

RUN apt-get update \
    && apt-get upgrade -y \
    && rm -rf /var/lib/apt/lists/*

# COPY requirements-hashed.txt .
COPY requirements-test-vuln-hashed.txt .
RUN python -m pip install --no-cache-dir --only-binary=:all: \
    --require-hashes -r requirements-hashed.txt

COPY main.py .

EXPOSE 8080

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]