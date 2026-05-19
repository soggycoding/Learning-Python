from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func, select

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

db = SQLAlchemy(app)

class Genres(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    
    game = db.relationship('Games', backref='genres', lazy=True)
    
    def to_dict(self):
        return {
            "id" : self.id,
            "name" : self.name
        }
        
    def to_dict_with_games(self):
        return {
            "id" : self.id,
            "name" : self.name,
            "games" : [g.to_dict() for g in self.game]
        }

class Games(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    synopsis = db.Column(db.String(60), nullable=False)
    rating = db.Column(db.Integer(), nullable=False)
    
    playthrough = db.relationship('Playthroughs', backref='games', lazy=True)
    genre_id = db.Column(db.Integer, db.ForeignKey('genres.id'), nullable=False)
    
    def to_dict(self):
        return {
            "id" : self.id,
            "name" : self.name,
            "synopsis" : self.synopsis,
            "rating" : self.rating
        }
    
    def to_dict_with_genre(self):
        return {
            "id" : self.id,
            "name" : self.name,
            "synopsis" : self.synopsis,
            "rating" : self.rating,
            "genre" : [g.to_dict() for g in self.genre_id]
        }

    def to_dict_with_playthrough(self):
        return {
            "id" : self.id,
            "name" : self.name,
            "synopsis" : self.synopsis,
            "rating" : self.rating,
            "playthrough" : [p.to_dict() for p in self.playthrough]
        }
        
class Playthroughs(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    progress = db.Column(db.String(), nullable=False)
    
    game_id = db.Column(db.Integer, db.ForeignKey('games.id'), nullable=False)
    def to_dict(self):
        return {
            "id" : self.id,
            "progress" : self.progress
        }
    
    def to_dict_with_game(self):
        return {
            "id" : self.id,
            "progress" : self.progress,
            "game" : [g.to_dict() for g in self.game_id]
        }
        
'''
with app.app_context():
    db.drop_all()
    db.create_all()
'''

@app.route('/genres', methods=['POST', 'GET'])
def add_genre():
    if request.method == 'POST':
        data = request.get_json()
        if 'name' not in data:
            return {"error": "Missing Required Field"}, 400
        if not data['name']:
            return {"error": "Missing Required Field"}, 400
        genre = Genres(name=data['name'])
        db.session.add(genre)
        db.session.commit()
        
        return genre.to_dict(), 201
    
    if request.method == 'GET':
        genres = Genres.query.all()
        genre_list = [genre.to_dict() for genre in genres]
        return {"genre" : genre_list}, 200

@app.route('/genres/<int:id>', methods=['PUT', 'GET', 'DELETE'])
def update_genre(id):
    if request.method == 'PUT':
        genres = Genres.query.filter_by(id=id).first()
        if not genres:
            return {"error" : "Genre not found"}, 404
        data = request.get_json()
        if 'name' not in data:
            return {"error" : "Missing Required Field"}, 400
        if not data['name']:
            return {"error" : "Missing Required Field"}, 400
        genres.name = data['name']
        db.session.commit()
        return genres.to_dict(), 200
    
    if request.method == 'GET':
        genres = Genres.query.filter_by(id=id).first()
        if not genres:
            return {"error" : "Genre not found"}, 404
        return {"genre" : genres.to_dict()}, 200
    
    if request.method == 'DELETE':
        genres = Genres.query.filter_by(id=id).first()
        if not genres:
            return {"error" : "Genre not found"}, 404
        db.session.delete(genres)
        db.session.commit()
        return {"message" : "Genre deleted successfully"}, 200
 
if __name__ == '__main__':
    app.run(debug=True)