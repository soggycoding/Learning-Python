#3rd project will be a Library API
'''
1. It should be 3 separate lists 
1.1 the first list should be the author, their country and id.
1.2 the second list should be the book's id, descriptitle, tion, author id, and publication date
1.3 find a way on how I will link both lists together with their ID to make sure the corresponding author gets to the right book
2. It should display the corresponding book with the author once called or added to the list
3. It should not accept empty data and must return an 404 error
4. It should also return a 400 error when entering an invalid ID such as /999
5. It should have a ID generator for when adding a book.
6. Can be updated through using their unique ID
- variables should always be lowered case
- URLS should also be lowered case
- remove dummy tasks from initial data
- CHECK FOR BUGS ALWAYS
- Variable names should be relevant
'''
from flask import Flask, request

app = Flask(__name__)
books = []
authors = []
library = [list(zip(authors, books))]

@app.route('/authors', methods=['GET', 'POST'])
def author():
    if request.method == 'POST':
        data = request.get_json()
        if 'author' not in data or 'country' not in data:
            return {"error": "Missing required fields"}, 400
        name = data['author']
        country = data['country']
        if not name or not country:
            return {"error": "Missing required fields"}, 400
        author = {'id': id_author(), 'author': name, 'country': country}
        authors.append(author)
        return author, 201
    
    if request.method == 'GET':
        return {"authors": authors}, 200
    
@app.route('/authors/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def author_id(id):
    if request.method == 'GET':
        for author in authors:
            if author['id'] == id:
                return author, 200
        return{"error": "Content not found"}, 404
    
    if request.method == 'PUT':
        for author in authors:
            if author['id'] == id:
                data = request.get_json()
                if 'author' not in data or 'country' not in data:
                    return {"error": "Missing required fields"}, 400
                if not data['author'] or not data['country']:
                    return {"error": "Missing required fields"}, 400
                author['author'] = data['author']
                author['country'] = data['country']
                return author, 200
        return{"error": "Content not found"}, 404
    
    if request.method == 'DELETE':
        for author in authors:
            if author['id'] == id:
                authors.remove(author)
                return {"message": "Author deleted successfully"}, 200
        return{"error": "Content not found"}, 404

@app.route('/books', methods=['GET', 'POST'])
def book():
    if request.method == 'POST':
        data = request.get_json()
        if 'title' not in data or 'description' not in data or 'publication_date' not in data or 'author_id' not in data:
            return {"error": "Missing required fields"}, 400
        title = data['title']
        description = data['description']
        publication = data['publication_date']
        author_id = data['author_id']
        if not title or not description or not publication or not author_id:
            return {"error": "Missing required fields"}, 400
        for author in authors:
            if author['id'] == author_id:
                book = {'id': id_books(), 'title': title, 'description': description, 'publication_date': publication, 'author_id': author_id}
                books.append(book)
                return book, 201 
        return {"error": "Content not found"}, 404
    
    if request.method == 'GET':
        return {"books": books}, 200

@app.route('/books/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def book_id(id):
    if request.method == 'GET':
        for book in books:
            if book['id'] == id:
                for author in authors:
                    if author['id'] != book['author_id']:
                        return  [book], 200
                return [author,book], 200
        return {"error": "Content not found"}, 404

    if request.method == 'PUT':
        for book in books:
            if book['id'] == id:
                data = request.get_json()
                if 'title' not in data or 'description' not in data or 'publication_date' not in data or 'ID' not in data:
                    return {"error": "Missing required fields"}, 400
                if not data['title'] or not data['description'] or not data['publication_date'] or not data['id']:
                    return {"error": "Missing required fields"}, 400
                book['title'] = data['title']
                book['description'] = data['description']
                book['publication_date'] = data['publication_date']
                book['id'] = data['id']
                return book, 200
        return {"error": "Content not found"}, 404
    
    if request.method == 'DELETE':
        for book in books:
            if book['id'] == id:
                books.remove(book)
                return {"message": "Book deleted successfully"}, 200
        return {"error": "Content not found"}, 404
def id_books():
    if not books:
        return 1
    else:
        ids = [book['id'] for book in books]
        return max(ids)+1

def id_author():
    if not authors:
        return 1
    else:
        ids = [author['id'] for author in authors]
        return max(ids)+1

if __name__ == '__main__':
    app.run(debug=True)