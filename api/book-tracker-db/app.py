from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Library(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(120), nullable=False)
    
    def __repr__(self):
        return f'<Books: {self.title}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description
        }
if __name__ == '__main__':
    with app.app_context():
        db.create_all()

@app.route('/books', methods=['POST', 'GET'])
def book_list():
    if request.method == 'POST':
        data = request.get_json()
        if 'title' not in data or 'description' not in data:
            return {"error": "Missing required fields"}, 400
        if not data['title'] or not data['description']:
            return {"error": "Missing required fields"}, 400
        new_books = Library(title=data['title'], description=data['description'])
        db.session.add(new_books)
        db.session.commit()
        return new_books.to_dict(), 201
    
    if request.method == 'GET':
        books = Library.query.all()
        book_lists = [book.to_dict() for book in books]
        return {'Books': book_lists}, 200

@app.route('/books/<int:id>', methods=['PUT', 'GET', 'DELETE'])
def book_update(id):
    if request.method == 'PUT':
        books = Library.query.filter_by(id=id).first()
        if not books:
            return {"error": "Content not found"}, 404
        data = request.get_json()
        if not data['title'] or not data['description']:
            return {"error": "Missing required fields"}, 400
        if 'title' not in data or 'description' not in data:
            return {"error": "Missing required fields"}, 400
        books.title = data['title']
        books.description = data['description']
        db.session.commit()
        return books.to_dict(), 200
    
    if request.method == 'GET':
        books = Library.query.filter_by(id=id).first()
        if not books:
            return {"error": "Content not found"}, 404
        return books.to_dict(), 200
    
    if request.method == 'DELETE':
        books = Library.query.filter_by(id=id).first()
        if not books:
            return {"error": "Content not found"}, 404
        db.session.delete(books)
        db.session.commit()
        return {"message": "Successfully removed the book"}, 200
    
if __name__ == '__main__':
    app.run(debug=True)