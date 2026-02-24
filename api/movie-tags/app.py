from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

db = SQLAlchemy(app)

# Junction table
MovieTags = db.Table('MovieTags',
                     db.Column('movie_id', db.Integer, db.ForeignKey('movies.id')),
                     db.Column('tag_id', db.Integer, db.ForeignKey('tags.id'))
                     )
# One-To-Many (Movies & Reviews)
class Movies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.String(120), nullable=False)
    
    reviews = db.relationship('Reviews', backref='movie', lazy=True)

    def to_dict(self):
        return {
            "title" : self.title,
            "description" : self.description
        }
    
    def to_dict_with_reviews(self):
        return {
            "title" : self.title,
            "description" : self.description,
            "reviews" : [review.to_dict() for review in self.reviews]
        }
    
    def to_dict_with_tags(self):
        return {
            "title" : self.title,
            "description" : self.description,
            "tags" : [tag.to_dict() for tag in self.tags]
        }
         

class Reviews(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    review = db.Column(db.String(80), unique=True, nullable=False)
    movie_id = db.Column(db.Integer, db.ForeignKey('movies.id'), nullable=False)
    
    def to_dict(self):
        return {
            "id": self.id,
            "review": self.review,
            "movie_id": self.movie_id
        }
    
    def to_dict(self):
        return {
            "id": self.id,
            "tag" : self.tag,
            "movie_id" : self.movie_id,
            "movie" : self.movie.title
        }

class Tags(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tag = db.Column(db.String(30), unique=True,nullable=False)
    
    movie = db.relationship('Movies', secondary=MovieTags, backref=db.backref('tags', lazy='dynamic'))
    
    def to_dict(self):
        return {
            "id" : self.id,
            "tag" : self.tag,
        }
'''   
with app.app_context():
    db.drop_all()
    db.create_all()
'''
@app.route('/movies', methods=['POST', 'GET'])
def add_movie():
    if request.method == 'POST':
        data = request.get_json()
        if 'title' not in data or 'description' not in data:
            return {"error": "Missing required fields"}, 400
        if not data['title'] or not data['description']:
            return {"error": "Missing required fields"}, 400
        movie = Movies(title=data['title'], description=data['description'])
        db.session.add(movie)
        db.session.commit()
        return movie.to_dict(), 201
    
    if request.method == 'GET': 
        movies = Movies.query.all()
        movie_list = [movie.to_dict() for movie in movies]
        return {"Movies": movie_list}, 200
    
@app.route('/movies/<int:id>', methods=['PUT', 'GET', 'DELETE'])
def movie_id(id):
    if request.method == 'PUT':
        movies = Movies.query.filter_by(id=id).first()
        if not movies:
            return {"error" : "Movie not found"}, 404
        data = request.get_json()
        if 'title' not in data or 'description' not in data:
            return {"error": "Missing required fields"}, 400
        if not data['title'] or not data['description'] not in data:
            return {"error": "Missing required fields"}, 400
        movies.title = data['title']
        movies.description = data['description']
        db.session.commit()
        return movies.to_dict(), 200
    
    if request.method == 'GET':
        movies = Movies.query.filter_by(id=id).first()
        if not movies:
            return {"error": "Movie not found"}, 404
        return {"Movie": movies.to_dict()}, 200
    
    if request.method == 'DELETE':
        movies = Movies.query.filter_by(id=id).first()
        if not movies:
            return {"error" : "Movie not found"}, 404
        db.session.delete(movies)
        db.session.commit()
        return {"message": "Movie successfully deleted"}, 200
    
@app.route('/reviews', methods=['POST', 'GET'])
def add_review():
    if request.method == 'POST':
        data = request.get_json()
        if 'review' not in data or 'movie_id' not in data:
            return {"error": "Missing required fields"}, 400
        if not data['review'] or not data['movie_id']:
            return {"error": "Missing required fields"}, 400
        reviews = Reviews(review=data['review'], movie_id=data['movie_id'])
        db.session.add(reviews)
        db.session.commit()
        return reviews.to_dict(), 201

    if request.method == 'GET':
        reviews = Reviews.query.all()
        review_list = [review.to_dict() for review in reviews]
        return {"Reviews": review_list}, 200

@app.route('/reviews/<int:id>', methods=['PUT', 'GET', 'DELETE'])
def review_id(id):
    if request.method == 'PUT':
        reviews = Reviews.query.filter_by(id=id).first()
        if not reviews:
            return {"error": "Review not found"}, 404
        data = request.get_json()
        if 'review' not in data or 'movie_id' not in data:
            return{"error": "Missing required fields"}, 400
        if not data['review'] or not data['movie_id']:
            return{"error": "Missing required fields"}, 400
        reviews.review = data['review']
        db.session.commit()
        return reviews.to_dict(), 200
    
    if request.method == 'GET':
        reviews = Reviews.query.filter_by(id=id).first()
        if not reviews:
            return {"error": "Review not found"}, 404
        return reviews.to_dict(), 200
    
    if request.method == 'DELETE':
        reviews = Reviews.query.filter_by(id=id).first()
        if not reviews:
            return {"errror": "Review not found"}, 404
        db.session.delete(reviews)
        db.session.commit()
        return {"message" : "Review deleted successfully"}, 200
    
@app.route('/tags', methods=['POST', 'GET'])
def add_tags():
    if request.method == 'POST':
        data = request.get_json()
        if 'tag' not in data:
            return {"error": "Missing required fields"}, 400
        if not data['tag']:
            return {"error": "Missing required fields"}, 400
        tags = Tags(tag=data['tag'])
        db.session.add(tags)
        db.session.commit()
        return tags.to_dict(), 201
    
    if request.method == 'GET':
        tags = Tags.query.all()
        tag_list = [tag.to_dict() for tag in tags]
        return {"Tags": tag_list}, 200

@app.route('/tags/<int:id>', methods=['PUT', 'GET', 'DELETE'])
def tags_id(id):
    if request.method == 'PUT':
        tags = Tags.query.filter_by(id=id).first()
        if not tags:
            return {"error": "Tag not found"}, 404
        data = request.get_json()
        if 'tag' not in data:
            return {"error" : "Missing required fields"}, 400
        if not data['tag']:
            return {"error" : "Missing required fields"}, 400
        tags.tag = data['tag']
        db.session.commit()
        return tags.to_dict(), 200
    
    if request.method == 'GET':
        tags = Tags.query.filter_by(id=id).first()
        if not tags:
            return {"error": "Tag not found"}, 404
        return {"Tag": tags.to_dict()}, 200
    
    if request.method == 'DELETE':
        tags = Tags.query.filter_by(id=id).first()
        if not tags:
            {"error": "Tag not found"}, 404
        db.session.delete(tags)
        db.session.commit()
        return {"message": "Tag successfully deleted"}, 200
    
@app.route('/movies/<int:movie_id>/tags', methods=['POST', 'GET'])
def movie_genre(movie_id):
    if request.method == 'POST':
        movie = Movies.query.filter_by(id=movie_id).first()
        if not movie:
            return {"error" : "Movie not found"}, 404
        
        data = request.get_json()
        if 'tag_id' not in data:
            return {"error" : "Missing required fields"}, 400
        if not data['tag_id']:
            return {"error" : "Missing required fields"}, 400
        tag_id = data['tag_id']
        
        tag = Tags.query.get(tag_id)
        if not tag:
            return {"error" : "Tag not found"}, 404
        if tag in movie.tags:
            return {"error" : "Tag already in the movie"}, 200
        
        movie.tags.append(tag)
        db.session.commit()
        
        return {
            'movie': movie.to_dict(),
            'tags': tag.to_dict()
        }, 201

    if request.method == 'GET':
        movie = Movies.query.filter_by(id=movie_id).first()
        if not movie:
            return {"error" : "Movie not found"}, 404
        
        return {
            'movie': movie.to_dict_with_tags()
        }, 200
if __name__ == '__main__':
    app.run(debug=True)