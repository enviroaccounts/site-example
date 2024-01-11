"""Routes for parent Flask app."""
from flask import current_app as app
from flask import render_template,redirect
from .plots import LandUses
from .plots import LandUsesCopy
from .plots import WildingPines
from .plots import PredatorType
from .plots import GhgAgri
from .plots import GhgEnergy
from .plots import LandUseChangeBuildUp
from .plots import LandUseChangeExoticForest
from .plots import GHGEmissionsBySector
from .plots import ClimateMakaroa
from .plots import GhgRemoval
from .plots import ClimateVarAero
from .plots import PredatorControl

app.jinja_env.globals.update(LandUses=LandUses)
app.jinja_env.globals.update(LandUsesCopy=LandUsesCopy)
app.jinja_env.globals.update(WildingPines=WildingPines)
app.jinja_env.globals.update(PredatorType=PredatorType)
app.jinja_env.globals.update(GhgAgri=GhgAgri)
app.jinja_env.globals.update(GhgEnergy=GhgEnergy)
app.jinja_env.globals.update(LandUseChangeBuildUp=LandUseChangeBuildUp)
app.jinja_env.globals.update(LandUseChangeExoticForest=LandUseChangeExoticForest)
app.jinja_env.globals.update(GHGEmissionsBySector=GHGEmissionsBySector)
app.jinja_env.globals.update(ClimateMakaroa=ClimateMakaroa)
app.jinja_env.globals.update(GhgRemoval=GhgRemoval)
app.jinja_env.globals.update(ClimateVarAero=ClimateVarAero)
app.jinja_env.globals.update(PredatorControl=PredatorControl)


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

