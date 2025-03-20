from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

# Initialize extensions
db = SQLAlchemy()
jwt = JWTManager()

def create_app():
    """
    Factory function to create and configure the Flask app.
    """
    app = Flask(__name__)

    # Load configuration from config.py
    app.config.from_pyfile('config.py')

    # Initialize extensions with the app
    db.init_app(app)
    jwt.init_app(app)

    # Register blueprints (routes)
    from .routes.user_routes import user_bp
    from .routes.asset_routes import asset_bp
    from .routes.order_routes import order_bp
    from .routes.portfolio_routes import portfolio_bp

    app.register_blueprint(user_bp)
    app.register_blueprint(asset_bp)
    app.register_blueprint(order_bp)
    app.register_blueprint(portfolio_bp)

    return app