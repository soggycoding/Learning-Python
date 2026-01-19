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
library = [list(zip(authors,books))]

@app.route('/library', methods=['GET', 'POST'])
def book_library():
    if request.method == 'GET':
        library = [list(zip(authors,books))]
        return {"Library": library}, 200
    
    if request.method == 'POST':
        data = request.get_json()
        author = data['Author']
        country = data['Country']
        new_author = {'ID': id_author(),'Author': author, 'Country': country}
        authors.append(new_author)
        book = data['Title']
        new_description = data['Description']
        publication_date = data['Publication']
        new_book = {'ID': id_book(), 'Title': book, 'Description': new_description, 'Publication': publication_date}
        books.append(new_book)

        return [new_author,new_book], 200
    
@app.route('/library/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def sorted_book(id):
    if request.method == 'GET':
        for book in books:
            if book['ID'] == id:
                for author in authors:
                    if author['ID'] == id:
                        return [author, book]
        return {"error": "Book not found"}, 404
    
    if request.method == 'PUT':
        for author in authors:
            if author['ID'] == id:
                data = request.get_json()
                author['Author'] = data['Author']
                author['Country'] = data['Country']
                update_author = {'ID': id, 'Author': author, 'Country': author}
                authors.append(update_author)
                for book in books:
                    if book['ID'] == id:
                        data = request.get_json()
                        book['Title'] = data['Title']
                        book['Description'] = data['Description']
                        book['Publication'] = data['Publication']
                        update_book = {'ID': id, 'Title': book, 'Description': book, 'Publication' : book}
                        books.append(update_book)
                        return [update_author, update_book]
        return {"error": "Book not found"}, 404
                
def id_book():
    if not books:
        return 1
    else:
        ids = [book['ID'] for book in books]
        return max(ids)+1
    
def id_author():
    if not authors:
        return 1
    else:
        ids = [author['ID'] for author in authors]
        return max(ids)+1
if __name__ == '__main__':
    app.run(debug=True)