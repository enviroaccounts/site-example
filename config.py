from os import environ


class Config:
    """Flask configuration variables."""
    # General Config
    ENVIRONMENT = environ.get("ENVIRONMENT")
    FLASK_APP = "wsgi.py"
    FLASK_DEBUG = environ.get("FLASK_DEBUG")
    SECRET_KEY = environ.get("SECRET_KEY")

    # Static Assets
    STATIC_FOLDER = "static"
    TEMPLATE_FOLDER = "templates"
