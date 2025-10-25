from flask import Flask, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

# MySQL Connection Config
db_config = {
    'host': 'localhost',
    'user': 'root',          # Change if your MySQL user is different
    'password': 'dnd12345#',          # Put your MySQL password here
    'database': 'streetlights_db'
}

@app.route('/streetlights', methods=['GET'])
def get_street_lights():
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT id, lat, lng, status FROM street_lights")
        data = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify(data)
    except mysql.connector.Error as err:
        return jsonify({"error": str(err)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)