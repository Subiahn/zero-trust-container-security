## 🧪 취약점 재현 방법

Dockerfile에서 setuptools/wheel 업그레이드 부분을 주석 처리하면 취약점을 확인할 수 있습니다.
```dockerfile
# Case #1: 취약한 버전 테스트
RUN pip install --no-cache-dir -r requirements.txt

# Case #2: 보안 강화 버전 (권장)
# RUN pip install --no-cache-dir --upgrade pip setuptools wheel && \
#     pip install --no-cache-dir -r requirements.txt
```

> 💡 CI/CD 파이프라인에서 Trivy 스캔 결과를 확인하여 차이를 비교할 수 있습니다.

---

