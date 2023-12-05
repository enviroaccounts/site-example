from flask import Flask, render_template




def init_app():
    """Init app core"""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    with app.app_context():
        from . import routes
        from .plots import LandUses
        dash_app = LandUses.init_dash(app)

        return dash_app
