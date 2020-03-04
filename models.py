import os
from sqlalchemy import Column, String, Integer
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import sys
import json
from app import *
from config import *


db = SQLAlchemy()

def db_init(app):
    app.config.from_object('config')
    db.app = app
    db.init_app(app)
    migrate = Migrate(app, db)
    db.create_all()

def reset_db():
    db.drop_all()
    db.create_all()

# Uncomment this to reset the DB.
# reset_db()

class Movie(db.Model):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    title = Column(String(50), nullable=False)
    release_date = Column(String(20), nullable=False)

    def __init__(self, title, release_date):
        self.title = title
        self.release_date = release_date

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
    

class Actor(db.Model):
    __tablename__ = 'actors'

    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    name = Column(String(50), nullable=False)
    age = Column(Integer, nullable=False)
    gender = Column(String(20), nullable=False)

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
