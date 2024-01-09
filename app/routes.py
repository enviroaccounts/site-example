"""Routes for parent Flask app."""
from flask import current_app as app
from flask import render_template,redirect
from .plots import LandUses
from .plots import LandUsesCopy
from .plots import WildingPines
from .plots import PredatorType


app.jinja_env.globals.update(LandUses=LandUses)
app.jinja_env.globals.update(LandUsesCopy=LandUsesCopy)
app.jinja_env.globals.update(WildingPines=WildingPines)
app.jinja_env.globals.update(PredatorType=PredatorType)


@app.route('/')
def home():
    return redirect("/landuse_change")

@app.route('/landuse_change')
def landuse_change():
    return render_template("pages/landuse_change.html")


@app.route('/acknowledgements')
def acknowledgements():
    return render_template("pages/acknowledgements.html")

@app.route('/climate_variables')
def climate_variables():
    return render_template("pages/climate_variables.html")

@app.route('/invasive_species')
def invasive_species():
    return render_template("pages/invasive_species.html")

@app.route('/social_well_being')
def social_well_being():
    return render_template("pages/social_well_being.html")

@app.route('/main')
def main():
    return render_template("pages/main.html")

@app.route('/greenhouse_gas_emissions')
def greenhouse_gas_emissions():
    return render_template("pages/greenhouse_gas_emissions.html")

@app.route('/water_quality')
def water_quality():
    return render_template("pages/water_quality.html")

@app.route('/index')
def index():
    return render_template("pages/index.html")

