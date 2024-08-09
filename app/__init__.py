from flask import Flask
from .calculator import GeometricCalculator
from .units import Units


def create_app():
    app = Flask(__name__)

    # You can add configuration settings here if needed
    # app.config.from_object('config.Config')

    # Register blueprints here if you decide to use them in the future
    # from .routes import main_bp
    # app.register_blueprint(main_bp)

    return app
