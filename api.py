from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

# Initialize Flask app
app = Flask(__name__)
app.config.from_object(Config)

# Initialize SQLAlchemy and Migrate
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Import and register routes
from routes.user_routes import user_routes
from routes.asset_routes import asset_routes
from routes.order_routes import order_routes
from routes.portfolio_routes import portfolio_routes

app.register_blueprint(user_routes)
app.register_blueprint(asset_routes)
app.register_blueprint(order_routes)
app.register_blueprint(portfolio_routes)

# Run the app
if __name__ == "__main__":
    app.run(debug=True)