from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

db = SQLAlchemy(app)
        
class Authors(db.Model):
    __tablename__ = 'authors'
    id = db.Column(db.Integer, primary_key=True)
    author_name = db.Column(db.String(50), unique=True, nullable=False)
    country = db.Column(db.String(120), nullable=False)
    books = db.relationship('Books', backref='author', lazy=True)
    
    def __repr__(self):
        return f'<Added: {self.author_name}'
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.author_name,
            'country': self.country
        }
    
class Books(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(120), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('authors.id'), nullable=False)
    
    def __repr__(self):
        return f'<Added: {self.title}>'
    
    def to_dict(self, include_author=True):
        data = {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'author_id': self.author_id
        }
        
        if include_author:
            data['author'] =  {
                'id': self.author.id,
                'author_name': self.author.author_name,
                'country': self.author.country
            }
            
        return data
'''
if __name__ == '__main__':
    with app.app_context():
        db.create_all()

with app.app_context():
    db.drop_all()
    db.create_all()    
''' 

@app.route('/books', methods=['POST', 'GET'])
def add_books():
    if request.method == 'POST':
        data = request.get_json()
        if 'title' not in data or 'description' not in data or 'author_id' not in data:
            return {"error": "Missing required fields"}, 400
        if not data['title'] or not data['description'] or not data['author_id']:
            return {"error": "Missing required fields"}, 400
        author = Authors.query.get(data['author_id'])
        if not author:
            return {"error": "Author not found"}, 404
        new_book = Books(title=data['title'], description=data['description'], author_id=data['author_id'])
        db.session.add(new_book)
        db.session.commit()
        return new_book.to_dict(include_author=False), 201

    if request.method == 'GET':
        books = Books.query.all()
        book_list = [book.to_dict(include_author=False) for book in books]
        return {"books": book_list}
    
@app.route('/books/<int:id>', methods=['PUT', 'GET', 'DELETE'])
def book_id(id):
    if request.method == 'PUT':
        books = Books.query.filter_by(id=id).first()
        if not books:
            return {"error": "Content not found"}, 404
        data = request.get_json()
        if 'title' not in data or 'description' not in data:
            return {"error": "Missing required fields"}, 400
        if not data['title'] or not data['description']:
            return {"error": "Missing required fields"}, 400
        author = Authors.query.get(data['author_id'])
        if not author:
            return {"error": "Author not found"}, 404
        books.title = data['title']
        books.description = data['description']
        books.author_id = data['author_id']
        db.session.commit()
        return books.to_dict(include_author=False), 200
    
    if request.method == 'GET':
        books = Books.query.filter_by(id=id).first()
        if not books:
            return {"error": "Content not found"}, 404
        return books.to_dict(), 200
    
    if request.method == 'DELETE':
        books = Books.query.filter_by(id=id).first()
        if not books:
            return {"error": "Content not found"}, 404
        db.session.delete(books)
        db.session.commit()
        return {"message": "Successfully removed"}, 200

@app.route('/authors', methods=['POST', 'GET'])
def add_authors():
    if request.method == 'POST':
        data = request.get_json()
        if 'author' not in data or 'country' not in data:
            return {"error": "Missing required fields"}, 400
        if not data['author'] or not data['country']:
            return {"error": "Missing required fields"}, 400
        new_author = Authors(author_name=data['author'], country=data['country'])
        db.session.add(new_author)
        db.session.commit()
        return new_author.to_dict(), 201

    if request.method == 'GET':
        authors = Authors.query.all()
        author_list = [author.to_dict() for author in authors]
        return {'authors': author_list}, 200

@app.route('/authors/<int:id>', methods=['PUT', 'GET', 'DELETE'])
def author_id(id):
    if request.method == 'PUT':
        authors = Authors.query.filter_by(id=id).first()
        if not authors:
            return {"error": "Content not found"}, 404
        data = request.get_json()
        if 'author' not in data or 'country' not in data:
            return {"error": "Missing required fields"}, 400
        if not data['author'] or not data ['country']:
            return {"error": "Missing required fields"}, 400
        authors.author_name = data['author']
        authors.country = data['country']
        db.session.commit()
        return authors.to_dict(), 200

    if request.method == 'GET':
        authors = Authors.query.filter_by(id=id).first()
        if not authors:
            return {"error": "Content not found"}, 404
        return authors.to_dict(), 200
    
    if request.method == 'DELETE':
        authors = Authors.query.filter_by(id=id).first()
        if not authors:
            return{"error": "Content not found"}, 404
        db.session.delete(authors)
        db.session.commit()
        return {"message": "Successfully removed"}, 200
    
if __name__ == '__main__':
    app.run(debug=True)