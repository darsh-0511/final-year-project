from flask import Blueprint, render_template, jsonify  # ← ADD jsonify HERE
from app.database import fetch_street_lights
from pages.graph_page import get_graph_data

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/streetlights')
def get_street_lights():
    data = fetch_street_lights()
    return jsonify(data)  # ← Now works

@bp.route('/graph')
def graph_page():
    graph_json, working, not_working, total = get_graph_data()
    return render_template('graph.html',
                           graph_json=graph_json,
                           working=working,
                           not_working=not_working,
                           total=total)