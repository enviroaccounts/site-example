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

@app.route('/home')
def main():
    return render_template("pages/home.html")

@app.route('/disclaimer')
def disclaimer():
    return render_template("pages/disclaimer.html")

@app.route('/story')
def story():
    return render_template("pages/story.html")

@app.route('/sponsorship')
def sponsorship():
    return render_template("pages/sponsorship.html")

@app.route('/reference')
def reference():
    return render_template("pages/reference.html")

@app.route('/acknowledgements')
def acknowledgements():
    return render_template("pages/acknowledgements.html")

@app.route('/background')
def background():
    return render_template("pages/background.html")

@app.route('/landuse_change')
def landuse_change():
    return render_template("pages/landuse_change.html",
                           related = {
                                    "climate_variables",
                                    "invasive_species",
                                    "social_well_being",
                                    "greenhouse_gas_emissions",
                                    "water_quality"
                                    },active="landuse_change"
                                    )

@app.route('/climate_variables')
def climate_variables():
    return render_template("pages/climate_variables.html",
                                    related = {
                                    "invasive_species",
                                    "social_well_being",
                                    "water_quality",
                                    },active="climate_variables"
                                    )


@app.route('/invasive_species')
def invasive_species():
    return render_template("pages/invasive_species.html",
                                    related = {
                                    "climate_variables",
                                    "water_quality",
                                    "landuse_change",
                                    },active="invasive_species")

@app.route('/social_well_being')
def social_well_being():
    return render_template("pages/social_well_being.html",
                                    related = {
                                    "climate_variables",
                                    "invasive_species",
                                    "greenhouse_gas_emissions",
                                    "water_quality"
                                    },active="social_well_being")

@app.route('/greenhouse_gas_emissions')
def greenhouse_gas_emissions():
    return render_template("pages/greenhouse_gas_emissions.html",
                                    related = {
                                    "climate_variables",
                                    "social_well_being",
                                    "water_quality",
                                    },active="greenhouse_gas_emissions")


@app.route('/water_quality')
def water_quality():
    return render_template("pages/water_quality.html",
                                    related = {
                                    "climate_variables",
                                    "social_well_being",
                                    "greenhouse_gas_emissions",
                                    "landuse_change"
                                    },active="water_quality")



