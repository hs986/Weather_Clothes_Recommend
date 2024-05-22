from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# Weather Service의 URL
WEATHER_SERVICE_URL = 'http://weather-service:5000/weather'

def recommend_clothing(temperature, description):
    """온도와 날씨 설명을 기반으로 옷차림을 추천"""
    if temperature < 0:
        return "Wear a heavy coat, scarf, and gloves."
    elif temperature < 10:
        return "Wear a coat and warm clothing."
    elif temperature < 20:
        return "Wear a jacket or sweater."
    elif temperature < 30:
        return "Wear light clothing."
    else:
        return "Wear shorts and a t-shirt."

@app.route('/recommendation', methods=['GET'])
def get_recommendation():
    city = request.args.get('city')
    if not city:
        return jsonify({'error': 'City is required'}), 400

    # Weather Service에 날씨 데이터를 요청
    response = requests.get(WEATHER_SERVICE_URL, params={'city': city})
    if response.status_code == 200:
        data = response.json()
        recommendation = recommend_clothing(data['temperature'], data['description'])
        return jsonify({
            'city': data['city'],
            'temperature': data['temperature'],
            'description': data['description'],
            'recommendation': recommendation
        })
    else:
        return jsonify({'error': 'Unable to fetch weather data'}), response.status_code

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)