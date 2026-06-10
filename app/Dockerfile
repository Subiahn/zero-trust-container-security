FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get upgrade -y && rm -rf /var/lib/apt/lists/*

# requirements.txt 해시 고정
COPY requirements.txt .
RUN pip install --no-cache-dir --only-binary :all: \
    pip==26.0.1 \
    setuptools==82.0.1 && \
    pip install --no-cache-dir --only-binary :all: \
    --require-hashes -r requirements.txt

COPY main.py .

EXPOSE 8080

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]