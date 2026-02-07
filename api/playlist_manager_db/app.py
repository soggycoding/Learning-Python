from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

db = SQLAlchemy(app)

SongPlaylist = db.Table('SongPlaylist',
                        db.Column('song_id', db.Integer, db.ForeignKey('songs.id')),
                        db.Column('playlist_id', db.Integer, db.ForeignKey('playlists.id'))
                        )
    
class Songs(db.Model):
    __tablename__ = 'songs'
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(30), unique=True, nullable=False)
    artist = db.Column(db.String(30), nullable=False)
    duration = db.Column(db.String(10), nullable=False)
    genre = db.Column(db.String(30), nullable=False)

    playlists = db.relationship('Playlists', secondary=SongPlaylist, backref=db.backref('songs', lazy='dynamic'))
    
    def __repr__(self):
        return f"<Added: {self.title}>"
    
    def to_dict(self):
        return {
            'id' : self.id,
            'title' : self.title,
            'artist' : self.artist,
            'duration' : self.duration,
            'genre' : self.genre,
        }

class Playlists(db.Model):
    __tablename__ = 'playlists'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(120), nullable=False)
    created_date = db.Column(db.DateTime, default=datetime.now)
    
    def __repr__(self):
        return f"<Added: {self.name}>"
    
    def to_dict(self):
       return {
            'id' : self.id,
            'name' : self.name,
            'description' : self.description,
            'created_date' : self.created_date
        }

with app.app_context():
    db.drop_all()
    db.create_all()

@app.route('/songs', methods=['POST', 'GET'])
def add_songs():
    if request.method == 'POST':
        data = request.get_json()
        if 'title' not in data or 'artist' not in data or 'duration' not in data or 'genre' not in data:
            return {"error": "Missing required fields"}, 400
        if not data['title'] or not data['artist'] or not data['duration'] or not data['genre']:
            return {"error": "Missing required fields"}, 400
        songs = Songs(title=data['title'], artist=data['artist'], duration=data['duration'], genre=data['genre'])
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
        songs = Songs.query.get(id)
        if not songs:
            return {"error": "Content not found"}, 404
        data = request.get_json()
        if 'title' not in data or 'artist' not in data or 'duration' not in data or 'genre' not in data:
            return {"error": "Missing required fields"}, 400
        if not data['title'] or not data['artist'] or not data['duration'] or not data['genre']:
            return {"error": "Missing required fields"}, 400
        songs.title = data['title']
        songs.artist = data['artist']
        songs.duration = data['duration']
        songs.genre = data['genre']
        db.session.commit()
        return songs.to_dict(), 200
    
    if request.method == 'GET':
        songs = Songs.query.get(id)
        if not songs:
            return {"error": "Content not found"}, 404
        return {"song":songs.to_dict()}, 200
    
    if request.method == 'DELETE':
        songs = Songs.query.get(id)
        if not songs:
            return {"error": "Content not found"}, 404
        db.session.delete(songs)
        db.session.commit()
        return {"message": "Successfully deleted"}, 200
      
@app.route('/playlists', methods=['POST', 'GET'])
def add_playlist():
    if request.method == 'POST':
        data = request.get_json()
        if 'name' not in data or 'description' not in data:
            return {"error": "Missing required fields"}, 400
        if not data['name'] or not data['description']:
            return {"error": "Missing required fields"}, 400
        playlists = Playlists(name=data['name'], description=data['description'])
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
        playlists = Playlists.query.get(id)
        if not playlists:
            return {"error": "Content not found"}, 404
        data = request.get_json()
        if 'name' not in data or 'description' not in data:
            return {"error": "Missing required fields"}, 400
        if not data['name'] or not data['description']:
            return {"error": "Missing required fields"}, 400
        playlists.name = data['name']
        playlists.description = data['description']
        db.session.commit()
        return playlists.to_dict(), 200
    
    if request.method == 'GET':
        playlists = Playlists.query.get(id)
        if not playlists:
            return {"error": "Content not found"}, 404
        
        song_list = [songs.to_dict() for songs in playlists.songs]
        return {"playlist": playlists.to_dict(), "songs": song_list}, 200
            
    if request.method == 'DELETE':
        playlists = Playlists.query.get(id)
        if not playlists:
            return {"error": "Content not found"}, 404
        db.session.delete(playlists)
        db.session.commit()
        return {"message": "Successfully deleted"}, 200

@app.route('/playlists/<int:playlist_id>/songs', methods=['POST'])
def add_song_to_playlist(playlist_id):
    playlist = Playlists.query.get(playlist_id)
    if not playlist:
        return {"error": "Playlist not found"}, 404
    
    data = request.get_json()
    if 'song_id' not in data:
        return {"error": "Missing required fields"}, 400
    if not data['song_id']:
        return {"error": "Missing required fields"}, 400
    song_id = data['song_id']
    
    song = Songs.query.get(song_id)
    if not song:
        return {"error": "Song not found"}, 404
    if song in playlist.songs:
        return {"message": "Song already in playlist"}, 200
    
    playlist.songs.append(song)
    db.session.commit()
    
    return {
        'playlist':playlist.to_dict(), 
        'song_added': song.to_dict()}, 201

@app.route('/playlists/<int:playlist_id>/songs/<song_id>', methods=['DELETE'])
def delete_song_from_playlist(playlist_id, song_id):
    playlist = Playlists.query.get(playlist_id)
    if not playlist:
        return {"error": "Playlist not found"}, 404
    
    song = Songs.query.get(song_id)
    if not song:
        return {"error": "Song not found"}, 404
    if song not in playlist.songs:
        return {"message": "Song is not in the playlist"}, 200
    
    playlist.songs.remove(song)
    db.session.delete(song)
    db.session.commit()
    
    return {"message": "Song removed from playlist successfully"}, 200

if __name__ == '__main__':
    app.run(debug=True)
    