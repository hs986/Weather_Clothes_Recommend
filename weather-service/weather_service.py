from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# OpenWeatherMap API 키 및 URL
API_KEY = 'your_api_key'
API_URL = 'http://api.openweathermap.org/data/2.5/weather'

@app.route('/weather', methods=['GET'])
def get_weather():
    # 요청에서 도시 이름을 가져옴
    city = request.args.get('city')
    if not city:
        return jsonify({'error': 'City is required'}), 400
    
    # OpenWeatherMap API에 요청을 보내 날씨 데이터를 가져옴
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric'  # 섭씨 온도로 반환
    }
    response = requests.get(API_URL, params=params)
    
    if response.status_code == 200:
        data = response.json()
        weather_info = {
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'city': data['name']
        }
        return jsonify(weather_info)
    else:
        return jsonify({'error': 'Unable to fetch weather data'}), response.status_code

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)