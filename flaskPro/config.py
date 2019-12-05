import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class Debug:
    SQLALCHEMY_DATABASE_URI = "sqlite:///"+os.path.join(BASE_DIR,"debug.sqlite")
    print(SQLALCHEMY_DATABASE_URI)
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    DEBUG = True
    USE_RELOADER = True