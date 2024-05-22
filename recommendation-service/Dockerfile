# 베이스 이미지로 Python 3.9 slim 버전을 사용
FROM python:3.9-slim

# 작업 디렉토리를 /app으로 설정
WORKDIR /app

# requirements.txt 파일을 컨테이너에 복사
COPY requirements.txt .

# 필요한 Python 패키지를 설치
RUN pip install -r requirements.txt

# 애플리케이션 소스 코드를 컨테이너에 복사
COPY recommendation_service.py .

# 애플리케이션을 실행
CMD ["python", "recommendation_service.py"]