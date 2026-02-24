Markdowns to remember: 
'#' For headings 
'-' for bullet points 
'code' for inline code 
'''code block''' for code blocks 
'[x]' for completed checkboxes 
'[]' for incomplete checkboxes

# MOVIE TAGS DATABASE(MANY-TO-MANY, ONE-TO-MANY)
- RESTFUL API Combines reviews, tags and rating suggestions

### PRE-REQUISITES
- Python
- Flask
- SQLAlchemy

### INSTALLATION

## TECHSTACK
- Python
- Flask
- SQLAlchemy

## DATANASE SCHEMA

## API ENDPOINTS

### REVIEWS
`POST /reviews` - Adds a new review
`GET /reviews` - Retrieves all the reviews
`PUT /reviews/<int:id>` - Updates a specific review
`GET /reviews/<int:id>` - Retrieves a specific review
`DELETE /reviews/int:id>` - Deletes a specific review

### TAGS
`POST /tags` - Adds a new tag
`GET /tags` - Retrieves all the tags
`PUT /tags/<int:id>` - Updates a specific tag
`GET /tags/<int:id>` - Retrieve a specific tag
`DELETE /tags/<int:id>` - Deletes a specific tag

### MOVIES
`POST /movies` - Adds a new movie
`GET /movies` - Retrives all the movies
`PUT /movies/<int:id>` - Updates a specific movie
`GET /movies/<int:id>` - Retrieves a specific movie
`DELETE /movies/<int:id>` - Deletes a specific movie

## PROJECT OVERVIEW AND FEATURES
- Connects one-to-many relationship and many-to-many relationship

## PROJECT STATUS
[x] PHASE 1: CRUD for Reviews and Tags
[x] PHASE 2: Validator
[x] PHASE 3: One-to-Many relationship
[x] PHASE 4: Many-to-Many relationship
[x] PHASE 5: Junction table for movies and tags
[] PHASE 6: