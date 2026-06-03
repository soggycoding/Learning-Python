Markdowns to remember:
'#' For headings 
'-' for bullet points 
'code' for inline code 
'''code block''' for code blocks 
'[x]' for completed checkboxes 
'[]' for incomplete checkboxes

Check list for API
POST:
[] Valid data - works? 
[] Missing required field - returns 400? 
[] Empty string - returns 400? 
[] Invalid foreign key (if applicable) - returns 404? 
[] Duplicate (if applicable) - returns appropriate error?

TESTING CHECKLIST
GET by ID: Valid ID - returns data? 
[] Non-existent ID - returns 404?

PUT:
Valid update - works? 
[] Non-existent ID - returns 404? 
[] Missing fields - returns 400? 
[] Invalid foreign key - returns 404?

DELETE:
Valid ID - deletes? 
[] Non-existent ID - returns 404?

Game Library Tracker API
A game library that tracks your progress, and also display the basic information about the game such as, the creator, ratings, synopsis, and ratings.

# PRE-REQUISITES
Flask Python SQLAlchemy

# INSTALLATION
TECHSTACK
Flask Python SQLAlchemy

# DATABASE SCHEMA
API ENDPOINTS
One-to-Many for returning nested data

## Genres (genres -> games)
POST /genres - Create a new genre
GET /genres - Retrieves all the genres 
PUT /genres/<int:id> - Updates a specific genre
GET /genres/<int:id> - Retrieves a specific genre
DELETE /genres/<int:id> - Deletes a specific genre

## Games (games -> playthrough)
POST /games - Create a new game 
GET /games - Retrieves all the Games 
PUT /games/<int:id> - Updates a specific game 
GET /games/<int:id> - Retrieves a specific game 
DELETE /games/<int:id> - Deletes a specific game

## Playthrough - (playthroughs)
POST /playthroughs - Create a new playthrough 
GET /playthroughs - Retrieves all playthroughs 
PUT /playthroughs/<int:id> - Updates a specific playthrough 
GET /playthroughs/<int:id> - Retrieves a specific playthrough 
DELETE /playthroughs/<int:id> - Delete a specific playthrough

# PROJECT OVERVIEW AND FEATURES
This project is just a refresher to understand how API's work again while learning something new.

# PROJECT STATUS
[x] Phase 1: CRUD for Genre
[x] Phase 2: CRUD for Games
[x] Phase 3: Validator for Genre and Games
[x] Phase 4: CRUD for Playthrough
[x] Phase 5: Validator for Playthrough
[x] Phase 6: Finish