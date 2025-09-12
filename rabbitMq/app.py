from flask import Flask, jsonify, request
from queue_manager import create_queues

app = Flask(__name__)

@app.route('/create_queues/<int:user_id>', methods=['POST'])
def create_queues_endpoint(user_id):
    """HTTP endpoint to create queues for a given user_id."""
    data = request.get_json(silent=True)  # Handle optional JSON body
    if data:
        print(f"Received data: {data}")  # Log for debugging
    success, message = create_queues(user_id)
    if success:
        return jsonify({"status": "success", "message": message}), 200
    else:
        return jsonify({"status": "error", "message": message}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)