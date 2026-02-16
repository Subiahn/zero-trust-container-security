# CVE 취약점이 있는 이미지
FROM python:3.11-slim

# 작업 디렉토리 설정
WORKDIR /app

# 의존성 파일 복사
COPY requirements.txt .


# # 의존성 설치
# RUN pip install --no-cache-dir -r requirements.txt

# setuptools와 wheel을 최신 버전으로 업그레이드하여 취약점 패치
RUN pip install --no-cache-dir --upgrade pip setuptools wheel && \
    pip install --no-cache-dir -r requirements.txt


# 애플리케이션 코드 복사
COPY app.py .

# 비root 사용자 생성 및 전환
RUN useradd -m -u 1000 appuser && \
    chown -R appuser:appuser /app

USER appuser

# 포트 노출
EXPOSE 8080

# 애플리케이션 실행
CMD ["python", "app.py"]