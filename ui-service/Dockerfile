# 베이스 이미지로 Node.js 14 버전을 사용
FROM node:14

# 작업 디렉토리를 /app으로 설정
WORKDIR /app

# package.json과 package-lock.json을 컨테이너에 복사
COPY package*.json ./

# 필요한 Node.js 패키지를 설치
RUN npm install

# 애플리케이션 소스 코드를 컨테이너에 복사
COPY . .

# 빌드 작업을 수행
RUN npm run build

# 빌드된 애플리케이션을 제공하기 위해 serve를 설치
RUN npm install -g serve

# 애플리케이션을 실행
CMD ["serve", "-s", "build"]

# 컨테이너가 사용할 포트를 노출
EXPOSE 5000
