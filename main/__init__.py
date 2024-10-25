from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os


db = SQLAlchemy()
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
    db.init_app(app)

    with app.app_context():
        # Import all models from models folder 
        from . import models
        db.create_all()
        

    return app