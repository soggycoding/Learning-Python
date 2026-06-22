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

# Restaurant and Review API
An API that gives the preview of the restaurant and its reviews.

# PRE-REQUISITES
Flask Python SQLAlchemy

# INSTALLATION
TECHSTACK
Flask Python SQLAlchemy

# DATABASE SCHEMA
API ENDPOINTS
two One-to-Many relationships for returning nested data

## Restaurant (restaurant -> MenuItem, Restaurant -> Review)
POST /restaurants - Create a new restaurant
GET /restaurants - Retrieves all the restaurants
PUT /restaurants/<int:id> - Updates a specific restaurant
GET /restaurants/<int:id> - Retrieves a specific restaurant
DELETE /restaurants/<int:id> - Deletes a specific restaurant

## Review (Restaurant -> Review)
POST /reviews - Create a new review
GET /reviews - Retrieves all the reviews
PUT /reviews/<int:id> - Updates a specific review 
GET /reviews/<int:id> - Retrieves a specific review
DELETE /reviews/<int:id> - Deletes a specific review

# PROJECT OVERVIEW AND FEATURES
This project is just a refresher to understand how API's work again while learning something new.

# PROJECT STATUS
[x] Phase 1: CRUD for Restaurant and Reviews
[] Phase 2: Validator for restaurant and reviews
[] Phase 3: Filtering the reviews for each restaurant
[] Phase 4: Finish