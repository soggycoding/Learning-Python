from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

db = SQLAlchemy(app)

SongPlaylist = db.Table('SongPlaylist',
                        db.Column('song_id', db.Integer, db.ForeignKey('songs.id'), primary_key=True),
                        db.Column('playlist_id', db.Integer, db.ForeignKey('playlists.id'), primary_key=True)
                        )
    
class Songs(db.Model):
    __tablename__ = 'songs'
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(30), unique=True, nullable=False)
    artist = db.Column(db.String(30), nullable=False)
    playlist_id = db.Column(db.Integer)
    playlists = db.relationship('Playlists', secondary=SongPlaylist, backref=db.backref('songs', lazy='dynamic'))
    
    def __repr__(self):
        return f"<Added: {self.title}>"
    
    def to_dict(self):
        return {
            'id' : self.id,
            'title' : self.title,
            'artist' : self.artist,
            'playlist_id' : self.playlist_id
        }
class Playlists(db.Model):
    __tablename__ = 'playlists'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    
    def __repr__(self):
        return f"<Added: {self.name}>"
    
    def to_dict(self):
       return {
            'id' : self.id,
            'name' : self.name
        }
'''
with app.app_context():
    db.drop_all()
    db.create_all()
'''
@app.route('/songs', methods=['POST', 'GET'])
def add_songs():
    if request.method == 'POST':
        data = request.get_json()
        if 'title' not in data or 'artist' not in data or 'playlist_id' not in data:
            return {"error": "Missing required fields"}, 400
        if not data['title'] or not data['artist'] or not data['playlist_id']:
            return {"error": "Missing required fields"}, 400
        playlists = Playlists.query.get(data['playlist_id'])
        if not playlists:
            return {"error": "Playlist not found"}, 404
        songs = Songs(title=data['title'], artist=data['artist'], playlist_id=data['playlist_id'])
        db.session.add(songs)
        db.session.commit()
        return songs.to_dict(), 201
    
    if request.method == 'GET':
        songs = Songs.query.all()
        songs_list = [song.to_dict() for song in songs]
        return {"songs": songs_list}, 200

@app.route('/songs/<int:id>', methods=['PUT', 'GET', 'DELETE'])
def songs_id(id):
    if request.method == 'PUT':
        songs = Songs.query.filter_by(id=id).first()
        if not songs:
            return {"error": "Content not found"}, 404
        data = request.get_json()
        if 'title' not in data or 'artist' not in data or 'playlist_id' not in data:
            return {"error": "Missing required fields"}, 400
        if not data['title'] or not data['artist'] or not data['playlist_id']:
            return {"error": "Missing required fields"}, 400
        playlists = Playlists.query.get(data['playlist_id'])
        if not playlists:
            return {"error": "Playlist not found"}, 404
        songs.title = data['title']
        songs.artist = data['artist']
        songs.playlist_id = data['playlist_id']
        db.session.commit()
        return songs.to_dict(), 200
    
    if request.method == 'GET':
        songs = Songs.query.filter_by(id=id).first()
        if not songs:
            return {"error": "Content not found"}, 404
        return songs.to_dict(), 200
    
    if request.method == 'DELETE':
        songs = Songs.query.filter_by(id=id).first()
        if not songs:
            return {"error": "Content not found"}, 404
        db.session.delete(songs)
        db.session.commit()
        return {"message": "Successfully deleted"}, 200
        
@app.route('/playlists', methods=['POST', 'GET'])
def add_playlist():
    if request.method == 'POST':
        data = request.get_json()
        if 'name' not in data:
            return {"error": "Missing required fields"}, 400
        if not data['name']:
            return {"error": "Missing required fields"}, 400
        playlists = Playlists(name=data['name'])
        db.session.add(playlists)
        db.session.commit()
        return playlists.to_dict(), 201
    
    if request.method == 'GET':
        playlists = Playlists.query.all()
        playlist_list = [playlist.to_dict() for playlist in playlists]
        return {"playlist": playlist_list}, 200

@app.route('/playlists/<int:id>', methods=['PUT', 'GET', 'DELETE'])
def playlist_id(id):
    if request.method == 'PUT':
        playlists = Playlists.query.filter_by(id=id).first()
        if not playlists:
            return {"error": "Content not found"}, 404
        data = request.get_json()
        if 'name' not in data:
            return {"error": "Missing required fields"}, 400
        if not data['name']:
            return {"error": "Missing required fields"}, 400
        playlists.name = data['name']
        db.session.commit()
        return playlists.to_dict(), 200
    
    if request.method == 'GET':
        playlists = Playlists.query.filter_by(id=id).first()
        if not playlists:
            return {"error": "Content not found"}, 404
        return playlists.to_dict(), 200
    
    if request.method == 'DELETE':
        playlists = Playlists.query.filter_by(id=id).first()
        if not playlists:
            return {"error": "Content not found"}, 404
        db.session.delete(playlists)
        db.session.commit()
        return {"message": "Successfully deleted"}, 200
if __name__ == '__main__':
    app.run(debug=True)
    