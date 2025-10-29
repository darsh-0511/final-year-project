from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__, static_folder='../static', template_folder='../templates')
    CORS(app)

    # Load config
    from config.settings import db_config
    app.config['DB_CONFIG'] = db_config

    # Register routes
    from app.routes import bp
    app.register_blueprint(bp)

    return app