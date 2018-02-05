import os

class Config:
    """
    General configuratins parent class
    """
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://pasaris:maisiewilliams7@localhost/pitchez'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    UPLOADED_PHOTOS_DEST = 'app/static/photos'

    # email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

class ProdConfig(Config):
    """
    Production configuration child class
    """
    pass

class TestConfig(Config):
#    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://pasaris:maisiewilliams7@localhost/pitchez_test' 
    pass

class DevConfig(Config):
    """
    Development config child class
    """

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://pasaris:maisiewilliams7@localhost/pitchez'

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}

