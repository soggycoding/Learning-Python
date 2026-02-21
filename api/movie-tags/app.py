from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

db = SQLAlchemy(app)

# Many-to-Many(Association Object)
class TagsReviews(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    review_id = db.Column('review_id', db.Integer, db.ForeignKey('review.id'))
    tag_id = db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'))
    
    review = db.relationship('Reviews', back_populates='tagsreviews')
    tag = db.relationship('Tags', back_populates='tagsreviews')


class Reviews(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    review = db.Column(db.String(80), unique=True, nullable=False)
    tagsreviews = db.relationship('TagsReviews', back_populates='review',
                                  cascade='all, delete-orphan')
    
    def to_dict(self):
        return {
            "id": self.id,
            "review": self.review
        }
class Tags(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tag = db.Column(db.String(30), unique=True,nullable=False)
    tagsreviews = db.relationship('TagsReviews', back_populates='tag',
                                  cascade='all, delete-orphan')
    
    def to_dict(self):
        return {
            "id": self.id,
            "tag" : self.tag
        }
class Movies(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.String(120), nullable=False)

with app.app_context():
    db.drop_all()
    db.create_all()

@app.route('/reviews', methods=['POST', 'GET'])
def add_review():
    if request.method == 'POST':
        data = request.get_json()
        if 'review' not in data:
            return {"error": "Missing required fields"}, 400
        if not data['review']:
            return {"error": "Missing required fields"}, 400
        reviews = Reviews(review=data['review'])
        db.session.add(reviews)
        db.session.commit()
        return reviews.to_dict(), 201






if __name__ == '__main__':
    app.run(debug=True)