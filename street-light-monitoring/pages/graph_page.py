from flask import render_template
from app.database import fetch_street_lights
import plotly.graph_objs as go
import plotly.utils
import json

def get_graph_data():
    lights = fetch_street_lights()
    total = len(lights)
    working = sum(1 for l in lights if l['status'] == 'working')
    not_working = total - working

    fig = go.Figure(data=[go.Pie(
        labels=['Working', 'Not Working'],
        values=[working, not_working],
        hole=0.4,
        marker_colors=['#4CAF50', '#E91E63'],
        textinfo='label+percent',
        hoverinfo='value'
    )])
    fig.update_layout(
        title="Street Light Status",
        font=dict(family="Segoe UI", size=14),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)'
    )
    graph_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graph_json, working, not_working, total