from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func, select

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

db = SQLAlchemy(app)

class Restaurants(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    location = db.Column(db.String(50), nullable=False)
    stars = db.Column(db.Integer(), nullable=False)
    description = db.Column(db.String(50), nullable=False)
    
    review = db.relationship('Reviews', backref='restaurants', lazy=True)
    
    def to_dict(self):
        return {
            "id" : self.id,
            "name" : self.name,
            "location" : self.location,
            "stars" : self.stars,
            "description" : self.description
        }
    
    def to_dict_with_reviews(self):
        return {
            "id" : self.id,
            "name" : self.name,
            "location" : self.location,
            "stars" : self.stars,
            "description" : self.description,
            "reviews" : [r.to_dict() for r in self.review]
        }
        
class Reviews(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    user = db.Column(db.String(), nullable=False)
    rating = db.Column(db.Integer(), nullable=False)
    comment = db.Column(db.Integer(), nullable=False)
    
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'), nullable=False)
    
    def to_dict(self):
        return {
            "id" : self.id,
            "name" : self.name,
            "rating" : self.rating,
            "comment" : self.comment
        }

with app.app_context():
    db.drop_all()
    db.create_all()
    
@app.route('/restaurants', methods=['POST', 'GET'])
def add_restaurant():
    if request.method == "POST":
        data = request.get_json()
        if "name" not in data or "location" not in data or "stars" not in data or "description" not in data:
            return {"error" : "Missing required fields"}, 400
        if not data["name"] or not data["location"] or not data["stars"] or not data["descriptiom"]:
            return {"error" : "Missing required fields"}, 400
        