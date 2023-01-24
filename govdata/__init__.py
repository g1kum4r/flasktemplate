from flask import Flask
from govdata import config

def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_object(config)
    from govdata.packages import bp as packages_blueprint
    app.register_blueprint(packages_blueprint)
    return app
