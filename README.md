Dockerfile 에사 아래 주석 처리된 부분을 주석 해제한 후 
setuptools와 wheel을 업그레이드 하는 부분을 주석 처리하면 
case#1을 확인 할 수 있습니다. 

참고

---
# # 의존성 설치
# RUN pip install --no-cache-dir -r requirements.txt

# setuptools와 wheel을 최신 버전으로 업그레이드하여 취약점 패치
RUN pip install --no-cache-dir --upgrade pip setuptools wheel && \
    pip install --no-cache-dir -r requirements.txt
---
