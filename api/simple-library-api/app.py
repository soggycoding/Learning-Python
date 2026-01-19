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
library = []

#GETS THE WHOLE LIST OF BOOKS AND AUTHORS, ADDS A NEW LIST OF AUTHOR AND THEIR BOOK
@app.route('/library', methods=['GET', 'POST'])
def book_library():
    if request.method == 'GET':
        library = [list(zip(authors,books))]
        return {"Library": library}, 200
    
    if request.method == 'POST':
        data = request.get_json()
        author = data['Author']
        country = data['Country']
        if author == "":
            return {"error": "Contents not found"}, 404
        elif country == "":
            return {"error": "Contents not found"}, 404
        new_author = {'ID': id_author(),'Author': author, 'Country': country}
        authors.append(new_author)
        book = data['Title']
        description = data['Description']
        publication = data['Publication']
        if book == "":
            return {"error": "Contents not found"}, 404
        elif description == "":
            return {"error": "Contents not found"}, 404
        elif publication == "":
            return {"error": "Contents not found"}, 404
        new_book = {'ID': id_book(), 'Title': book, 'Description': description, 'Publication': publication}
        books.append(new_book)

        return [new_author,new_book], 200
#GET THE AUTHOR AND BOOK BY THEIR UNIQUE GENERATED ID, CAN UPDATE THEIR CONTENTS USING THEIR UNIQUE ID, CAN DELETE THEIR REQUESTED BOOK AND AUTHOR USING THEIR ID
@app.route('/library/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def sorted_book(id):
    if request.method == 'GET':
        for author in authors:
            if author['ID'] == id:
                for book in books:
                    if books['ID'] == id:
                        return [author, book]
        return {"error": "Contents not found"}, 404
    
    if request.method == 'PUT':
        for author in authors:
            if author['ID'] == id:
                authors.remove(author)
                data = request.get_json()
                author['Author'] = data['Author']
                author['Country'] = data['Country']
                if author == "":
                    return {"error": "Contents not found"}, 404
                authors.append(author)
                for book in books:
                    if book['ID'] == id:
                        books.remove(book)
                        data = request.get_json()
                        book['Title'] = data['Title']
                        book['Description'] = data['Description']
                        book['Publication'] = data['Publication']
                        if book == "":
                            return {"error": "Contents not found"}, 404
                        books.append(book)
                        return [author, book]
        return {"error": "Contents not found"}, 404
                
    if request.method == 'DELETE':
        for author in authors:
            if author['ID'] == id:
                authors.remove(author)
                for book in books:
                    if book['ID'] == id:
                        books.remove(book)
                        return "Success", 200
        return {"error": "Contents not found"}, 404
                
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