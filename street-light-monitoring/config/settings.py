import os
from dotenv import load_dotenv

# MySQL Connection Config (password from .env)
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': os.getenv('DB_PASSWORD'),  # ← From .env
    'database': 'streetlights_db'
}