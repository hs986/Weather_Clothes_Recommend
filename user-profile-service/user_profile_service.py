from flask import Flask, jsonify, request
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/user_profiles"
mongo = PyMongo(app)

@app.route('/profile', methods=['POST'])
def create_profile():
    data = request.json
    user_id = data.get('user_id')
    profile = {
        'user_id': user_id,
        'location': data.get('location'),
        'preferred_style': data.get('preferred_style'),
        'recommendation_history': []
    }
    mongo.db.profiles.insert_one(profile)
    return jsonify({'message': 'Profile created successfully'}), 201

@app.route('/profile/<user_id>', methods=['GET'])
def get_profile(user_id):
    profile = mongo.db.profiles.find_one({'user_id': user_id})
    if profile:
        return jsonify(profile)
    else:
        return jsonify({'message': 'Profile not found'}), 404

@app.route('/profile/<user_id>/history', methods=['POST'])
def add_recommendation_history(user_id):
    recommendation = request.json.get('recommendation')
    mongo.db.profiles.update_one({'user_id': user_id}, {'$push': {'recommendation_history': recommendation}})
    return jsonify({'message': 'Recommendation history updated'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
