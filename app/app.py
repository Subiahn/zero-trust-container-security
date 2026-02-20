from flask import Flask, jsonify
import os
import random

app = Flask(__name__)

# ❌ 하드코딩된 크리덴셜 - SonarQube가 잡아냅니다
DB_PASSWORD = "super_secret_password_123"
SECRET_KEY = "hardcoded-secret-key"

@app.route('/')
def hello():
    return jsonify({
        'message': 'Hello from Zero Trust Container!',
        'version': '1.0.0',
        'hostname': os.environ.get('HOSTNAME', 'unknown')
    })

@app.route('/health')
def health():
    return jsonify({'status': 'healthy'}), 200

# ❌ SQL Injection 취약점 - SonarQube가 잡아냅니다
@app.route('/user/<username>')
def get_user(username):
    query = "SELECT * FROM users WHERE name = '" + username + "'"
    return jsonify({'query': query})

# ❌ 안전하지 않은 난수 생성 - SonarQube가 잡아냅니다
@app.route('/token')
def generate_token():
    token = str(random.randint(100000, 999999))
    return jsonify({'token': token})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)