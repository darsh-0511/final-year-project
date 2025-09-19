from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes to allow cross-origin requests

# Sample street light data
street_lights = [
    {"id": 1, "lat": 12.9716, "lng": 77.5946, "status": "working"},
    {"id": 2, "lat": 12.9750, "lng": 77.5900, "status": "not working"},
    {"id": 3, "lat": 12.9700, "lng": 77.6000, "status": "working"},
    {"id": 4, "lat": 12.9680, "lng": 77.5950, "status": "not working"}
]

@app.route('/streetlights', methods=['GET'])
def get_street_lights():
    return jsonify(street_lights)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)