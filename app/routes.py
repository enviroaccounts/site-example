"""Routes for parent Flask app."""
from flask import current_app as app
from flask import render_template
from .plots import LandUses
from .plots import LandUsesCopy


app.jinja_env.globals.update(LandUses=LandUses)
app.jinja_env.globals.update(LandUsesCopy=LandUsesCopy)


@app.route('/')
def index():
    return render_template('pages/index.html')



@app.route('/<page>')
def main(page):
    return render_template(f"pages/{page}.html")


@app.route('/water')
def water():
    return render_template('pages/water/index.html')
