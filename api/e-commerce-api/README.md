Markdowns to remember: 
'#' For headings 
'-' for bullet points 
'code' for inline code 
'''code block''' for code blocks 
'[x]' for completed checkboxes 
'[]' for incomplete checkboxes

# Check list for API

## POST:

[] Valid data - works? 
[] Missing required field - returns 400? 
[] Empty string - returns 400? 
[] Invalid foreign key (if applicable) - returns 404? 
[] Duplicate (if applicable) - returns appropriate error?

## TESTING CHECKLIST
GET by ID:
Valid ID - returns data?
[] Non-existent ID - returns 404?

## PUT:
Valid update - works?
[] Non-existent ID - returns 404? 
[] Missing fields - returns 400? 
[] Invalid foreign key - returns 404?

## DELETE:
Valid ID - deletes?
[] Non-existent ID - returns 404?

# E-Commerce API
A simple e-commerce API that will check the stocks, the orders, the status of the orders and the status of the stocks.

## PRE-REQUISITES
Flask
Python
SQLAlchemy

### INSTALLATION

# TECHSTACK
Flask
Python
SQLAlchemy

# DATABASE SCHEMA

# API ENDPOINTS
<-> Many to Many
-> One to many

### PRODUCTS (Products <-> Categories)
`POST /products` - Create a new product
`GET /products` - Retrieves all the products
`PUT /products/<int:id>` - Updates a specific product
`GET /products/<int:id>` - Retrieves a specific product
`DELETE /products/<int:id>` - Deletes a specific product

### CATEGORIES
`POST /categories` - Create a new category
`GET /categories` - Retrieves all the categories
`PUT /categories/<int:id>` - Updates a specific category
`GET /categories/<int:id>` - Retrieves a specific category
`DELETE /categories/<int:id>` - Deletes a specific product

### ORDERS - (Orders -> OrderItems)
`POST /orders` - Create a new order
`GET /orders` - Retrieves all orders
`PUT /orders/<int:id>` - Updates a specific order
`GET /orders/<int:id>` - Retrieves a specific order
`DELETE /orders/<int:id>` - Delete a specific order

### ORDERITEMS - (OrderItems -> Products)

# PROJECT OVERVIEW AND FEATURES
This project will help me to understand all the relationships better and solidify my knowledge for each relationships

# PROJECT STATUS
[x] Phase 1: CRUD for products, categories, and orders
[x] Phase 2: Validator for all CRUDS and right placement of validators
[x] Phase 3: Junction table
[x] Phase 4: Many-to-many
[x] Phase 5: One-to-many
[] Phase 6:
