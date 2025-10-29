import mysql.connector
from flask import current_app

def get_db_connection():
    return mysql.connector.connect(**current_app.config['DB_CONFIG'])

def fetch_street_lights():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT id, lat, lng, status FROM street_lights")
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return data