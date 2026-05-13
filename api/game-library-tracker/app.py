from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func, select

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

db = SQLAlchemy(app)

class Genre(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    
    def to_dict(self):
        return {
            "id" : self.id,
            "name" : self.name
        }

class Game(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    synopsis = db.Column(db.String(60), nullable=False)
    
    def to_dict(self):
        return {
            "id" : self.id,
            "name" : self.name,
            "synopsis" : self.synopsis
        }