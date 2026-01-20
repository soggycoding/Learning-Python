#3rd project will be a Library API
'''
1. It should be 3 separate lists 
1.1 the first list should be the author, their country and id.
1.2 the second list should be the book's id, title, description, author id, and publication date
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
        name = data['Author']
        country = data['Country']
        if name == "":
            return {"error": "Content not found"}, 400
        elif country == "":
            return {"error": "Content not found"}, 400
        author = {'ID': id_author(), 'Author': name, 'Country': country}
        authors.append(author)
        return author, 200
    if request.method == 'GET':
        return {"Authors": authors}, 200
    
@app.route('/authors/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def author_id(id):
    if request.method == 'GET':
        for author in authors:
            if author['ID'] == id:
                return author, 200
        return{"error": "Content not found"}, 404
'''           
def id():
    if not books:
        return 1
    else:
        ids = [book['ID'] for book in books]
        return max(ids)+1
'''
def id_author():
    if not authors:
        return 1
    else:
        ids = [author['ID'] for author in authors]
        return max(ids)+1

if __name__ == '__main__':
    app.run(debug=True)