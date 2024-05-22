# Weather_Clothes_Recommendation
프로젝트 구성 요소

Weather Service
기능: 외부 날씨 API를 호출하여 날씨 데이터를 수집하고 제공.
docker build -t weather-service .
docker run -p 5000:5000 weather-service


Recommendation Service
기능: Weather Service로부터 날씨 데이터를 받아서 적절한 옷차림을 추천.
docker build -t recommendation-service .
docker run -p 5001:5001 recommendation-service


User Interface (UI) Service
기능: 사용자가 입력한 도시에 대한 날씨와 옷차림 추천 결과를 시각적으로 제공.
프론트엔드 기술: React.js, Angular, Vue.js 등.
docker build -t ui-service .
docker run -p 3000:3000 ui-service



User Profile Service
기능: 사용자의 프로필 데이터를 관리하고 개인화된 추천 제공.
docker build -t user-profile-service .
docker run -p 5002:5002 user-profile-service



Notification Service
기능: 사용자가 새로운 날씨 업데이트나 추천 결과를 알림 받을 수 있도록 지원.
docker build -t notification-service .
docker run -p 5003:5003 notification-service
