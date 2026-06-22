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
            "user" : self.user,
            "rating" : self.rating,
            "comment" : self.comment,
            "restaurant_id" : self.restaurant_id
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
        if not data["name"] or not data["location"] or not data["stars"] or not data["description"]:
            return {"error" : "Missing required fields"}, 400
        restaurant = Restaurants(name=data['name'], location=data['location'], stars=data['stars'], description=data['description'])
        db.session.add(restaurant)
        db.session.commit()
        return restaurant.to_dict(), 201
    
    if request.method == "GET":
        restaurants = Restaurants.query.all()
        restaurant_list = [restaurant.to_dict() for restaurant in restaurants]
        return {"restaurant": restaurant_list}, 200

@app.route('/restaurants/<int:id>', methods=['PUT', 'GET', 'DELETE'])
def update_restaurant(id):
    if request.method == "PUT":
        restaurant = Restaurants.query.filter_by(id=id).first()
        if not restaurant:
            return {"error":"Restaurant not found"}, 404
        data = request.get_json()
        if "name" not in data or "location" not in data or "stars" not in data or "description" not in data:
            return {"error" : "Missing required fields"}, 400
        if not data["name"] or not data["location"] or not data["stars"] or not data["descriptiom"]:
            return {"error" : "Missing required fields"}, 400
        restaurant.name = data['name']
        restaurant.location = data['location']
        restaurant.stars = data['stars']
        restaurant.description = data['description']
        db.session.commit()
        return restaurant.to_dict(), 200
    
    if request.method == "GET":
        restaurant = Restaurants.query.filter_by(id=id).first()
        if not restaurant:
            return {"error" : "Restaurant not found"}, 404
        return {"restaurant": restaurant.to_dict()}, 200
    
    if request.method == "DELETE":
        restaurant = Restaurants.query.filter_by(id=id).first()
        if not restaurant:
            return {"error" : "Restaurant not found"}, 404
        db.session.delete(restaurant)
        db.session.commit()
        return {"message" : "Restaurant successfully deleted"}, 200

@app.route('/reviews', methods=['POST', 'GET'])
def add_reviews():
    if request.method == "POST":
        data = request.get_json()
        if "user" not in data or "rating" not in data or "comment" not in data or "restaurant_id" not in data:
            return {"error" : "Missing required fields"}, 400
        if not data['user'] or not data['rating'] or not data['comment'] or not data['restaurant_id']:
            return {"error" : "Missing required fields"}, 400
        review = Reviews(user=data['user'], rating=data['rating'], comment=data['comment'], restaurant_id=data["restaurant_id"])
        db.session.add(review)
        db.session.commit()
        return review.to_dict(), 201
    
    if request.method == "GET":
        reviews = Reviews.query.all()
        review_list = [review.to_dict() for review in reviews]
        return {"reviews" : review_list}, 200

@app.route('/reviews/<int:id>', methods=['PUT', 'GET', "DELETE"])
def update_reviews(id):
    if request.method == "PUT":
        review = Reviews.query.filter_by(id=id).first()
        if not review:
            return  {"error" : "Review not found"}, 404
        data = request.get_json()
        if "user" not in data or "rating" not in data or "comment" not in data or "restaurant_id" not in data:
            return {"error" : "Missing required fields"}, 400
        if not data['user'] or not data['rating'] or not data['comment'] or not data['restaurant_id']:
            return {"error" : "Missing required fields"}, 400
        review.user = data['user']
        review.rating = data['rating']
        review.comment = data['comment']
        review.restaurant_id = data['restaurant_id']
        db.session.commit()
        return review.to_dict(), 200
    
    if request.method == "GET":
        review = Reviews.query.filter_by(id=id).first()
        if not review:
            return {"error" : "Review not found"}, 404
        return review.to_dict(), 200
    
    if request.method == "DELETE":
        review = Reviews.query.filter_by(id=id).first()
        if not review:
            return {"error" : "Review not found"}, 404
        db.session.delete(review)
        db.session.commit()
        return {"message" : "Review successfully deleted"}, 200
        
if __name__ == '__main__':
    app.run(debug=True)