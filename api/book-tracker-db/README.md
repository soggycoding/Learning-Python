Markdowns to remember:

'#' For headings
'-' for bullet points
'code' for inline code
'''code block''' for code blocks
'[x]' for completed checkboxes  
'[]' for incomplete checkboxes

# BOOK-TRACKER DATABASE
This will be the 2nd time I will convert one of my hardcoded API project into DB, this time I will be converting my book tracker API

## THINGS  TO CONSIDER
- This project will still use the CRUD principle
- This will implement the DRY method to avoid excessive codeblocks

## PROJECT OVERVIEW
- This will help me get used to using DB even more
- This conversion will also help me boost my confidence in doing database

# ENDPOINTS

### BOOK:
- POST /books: Creates a new book that has the 'title', 'description', and 'id'
- GET /books: Retrieve all the books including their contents
- PUT /books/<int:id>: Updates a specific book's content
- GET /books/<int:id>: Retrieves a specific book
- DELETE /books/<int:id>: Deletes a specific book

# PROJECT STATUS:
- [x] PHASE 1: Implement CRUD in books
- [x] PHASE 2: Include a validator before commiting it into DB