"""Routes for parent Flask app."""
from flask import current_app as app
from flask import render_template
from .plots.LandUses import create_figure


app.jinja_env.globals.update(create_figure=create_figure)


@app.route('/')
def index():
    return render_template('index.html')
