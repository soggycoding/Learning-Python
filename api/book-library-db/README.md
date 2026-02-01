Markdowns to remember: 
'#' For headings 
'-' for bullet points 
'code' for inline code 
'''code block''' for code blocks 
'[x]' for completed checkboxes 
'[]' for incomplete checkboxes

# BOOK-LIBRARY DATABASE
- This is a book libary API that will be using a DB to store its data

## THINGS TO CONSIDER:
- Books should have CRUD principle
- Authors should have CRUD principle
- It should connect the books with their respectful authors
- Validator for both author and books
- When displaying a book without an author, it should display the book but the author as null

## PROJECT OVERVIEW:
- With this 3rd conversion it should help me with a new feature that is using "relationship()" and I should also learn how to customize their behaviors and such.
- It should also help me more on having a more solid understanding of using DB
- 

# ENDPOINTS

## BOOKS:
- 'POST /books': This should post the books with their title, and description.
- 'GET /books': This should retrieve all the books 
- 'PUT /books/<int:id>': Updates a specific book's title or description
- 'GET /books/<int:id>': Retrieves a specific book 
- 'DELETE /books/<int:id>': Deletes a specific book

## AUTHORS:
- 'POST /authors': Add the authors name and country of origin
- 'GET /authors': Retrieves all the authors
- 'PUT /authors/<int:id>': Updates a specific authors name or country of origin
- 'GET /authors/<int:id>': Retrieves a specific author with their information
- 'DELETE /authors/<int:id>': Delete a specific author

# PROJECT STATUS
- [x] PHASE 1: A CRUD for the books and author
- [x] PHASE 2: Validator
- [x] PHASE 3: Mapping both database to eachother
- [] PHASE 4: