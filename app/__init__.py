from flask import Flask, render_template




def init_app():
    """Init app core"""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.Config')

    with app.app_context():
        from . import routes
        return app
