import os
import secrets
from fastapi import FastAPI
from pydantic import BaseModel



app = FastAPI(
    title="Zero Trust Container Security",
    description="Zero Trust 기반 컨테이너 보안 실습 앱",
    version="1.0.0"
)


class HealthResponse(BaseModel):
    status: str


class InfoResponse(BaseModel):
    message: str
    version: str
    hostname: str


class TokenResponse(BaseModel):
    token: str


@app.get("/", response_model=InfoResponse)
def root() -> InfoResponse:
    return InfoResponse(
        message="Hello from Zero Trust Container!",
        version="1.0.0",
        hostname=os.environ.get("HOSTNAME", "unknown")
    )


@app.get("/health", response_model=HealthResponse)
def health() -> HealthResponse:
    return HealthResponse(status="healthy")


@app.get("/token", response_model=TokenResponse)
def generate_token() -> TokenResponse:
    # 암호학적으로 안전한 난수 생성
    token = secrets.token_hex(32)
    return TokenResponse(token=token)