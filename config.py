import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    # Database configuration
    SQL_SERVER = os.getenv('DESKTOP-QJ09A7U')  # 'DESKTOP-QJ09A7U'
    SQL_DATABASE = os.getenv('TradingDB')  # 'TradingDB'
    SQL_DRIVER = os.getenv('ODBC Driver 17 for SQL Server')  # 'ODBC Driver 17 for SQL Server'
    SQL_USERNAME = os.getenv('SQL_USERNAME')
    SQL_PASSWORD = os.getenv('SQL_PASSWORD')
    SQLALCHEMY_DATABASE_URI = f"mssql+pyodbc://{SQL_USERNAME}:{SQL_PASSWORD}@{SQL_SERVER}/{SQL_DATABASE}?driver={SQL_DRIVER}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # JWT configuration
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False