import os

class Config:
    """
    General configurations parent class
    """
    SECRET_KEY = os.environ.get('SECRET_KEY')   
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://Pasaris:maisiewilliams7@localhost/pitchez' 
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOADED_PHOTOS_DEST = 'app/static/photos'   

class ProdConfig(Config):
    """
    Production configuration child class
    """
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")   

class TestConfig(Config):
   SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://Pasaris:maisiewilliams7@localhost/pitchez_test'
    

class DevConfig(Config):
    """
    Development config child class
    """
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://Pasaris:maisiewilliams7@localhost/pitchez'

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}