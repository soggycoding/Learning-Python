from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

db = SQLAlchemy(app)

class SongPlaylist(db.Table):
    __tablename__ = 'song_playlist'
    id = db.Column(db.Integer, primary_key=True)
    song_id = db.Column('song_id', db.Integer, db.ForeignKey('songs.id'))
    playlist_id = db.Column('playlist_id', db.Integer, db.ForeignKey('playlists.id'))
    
class Songs(db.Model):
    __tablename__ = 'songs'
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(30), unique=True, nullable=False)
    artist = db.Column(db.String(30), nullable=False)
    playlists = db.relationship('Playlists', secondary='song_playlist')
    
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
    songs = db.relationship('Songs', secondary='song_playlist')
    
    def __repr__(self):
        return f"<Added: {self.name}>"
    
    def to_dict(self):
        {
            'id' : self.id,
            'name' : self.name
        }
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
'''
if __name__ == '__main__':
    app.run(debug=True)