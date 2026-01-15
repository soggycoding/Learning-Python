from flask import Flask, make_response, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
books = [{'id': 1, 'title': "Cooking with Roger", 'description': "A cooking book starring Roger"},
         {'id': 2, 'title': "Drama with Darwin", 'description': "A book filled with drama starring Darwin"}]

@app.route('/books', methods=['GET', 'POST'])
def book_list():
    if request.method == 'GET':
        return {"books": books}, 200

    if request.method == "POST":
        data = request.get_json()
        title = data['title']
        description = data['description']
        new_book = {'id': get_next_id(), 'title': title, 'description': description}
        books.append(new_book)
        return new_book, 201
    
    
@app.route('/books/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def id_books(id): 
    if request.method == 'GET':
        for book in books: 
            if book['id'] == id:
                return book

        return "Could not find anything"
    if request.method == 'PUT':
        for book in books:
            if book['id'] == id:
                data = request.get_json()
                new_title = data['title']
                new_description = data['description']
                book.update({'title': new_title, 'description': new_description})
                return book, 200
        else:
            return{"error": "Book not found"}, 404
    if request.method == 'DELETE':
        for book in books:
            if book['id'] == id:
                books.remove(book)
                return "Removed succesfully\n", 200
        else:
            return{"error": "Book not found"}, 404
def get_next_id():
    if not books:
        return 1
    else:
        ids = [book['id'] for book in books]
        return max(ids)+1
    
if __name__ == '__main__': 
    app.run(debug=True)