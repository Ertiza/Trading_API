import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    # SQL Server Configuration
    SERVER = os.getenv('SERVER', 'DESKTOP-QJO9A7U')  # Default to your server name
    DATABASE = os.getenv('DATABASE', 'TradingDB')     # Default to your database name
    DRIVER = os.getenv('DRIVER', 'ODBC Driver 17 for SQL Server')  # Default to your driver
    USERNAME = os.getenv('DB_USERNAME', 'your_username')  # Add your SQL Server username
    PASSWORD = os.getenv('DB_PASSWORD', 'your_password')  # Add your SQL Server password

    # Construct the connection string
    SQLALCHEMY_DATABASE_URI = f"mssql+pyodbc://{USERNAME}:{PASSWORD}@{SERVER}/{DATABASE}?driver={DRIVER}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # JWT Configuration
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'your_jwt_secret_key')