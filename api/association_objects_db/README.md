Markdowns to remember: 
'#' For headings 
'-' for bullet points 
'code' for inline code 
'''code block''' for code blocks 
'[x]' for completed checkboxes 
'[]' for incomplete checkboxes

# ASSOCIATION OBJECTS DATABASE

## SHOPPING_ADD_TO_CART
- 3rd many-to-many project. Now tackling more on association objects(adding items with quantities)

## TECHSTACK
- Flask, Python, SQLAlchemy

## API ENDPOINTS

### CARTS
- `POST /CARTS` : Adds a new cart
- `GET /CARTS` : Retrieves all carts
- `PUT /CARTS<int:id>` : Updates a specific cart
- `GET /CARTS<int:id>` : Retrieves a specific cart with all the items in it
- `DELETE /CARTS<int:id>` : Delete a specific cart

### ITEMS
- `POST /ITEMS` : Adds a new item
- `GET /ITEMS` : Retrieves all items
- `PUT /ITEMS/<int:id>` : Update a specific item
- `GET /ITEMS/<int:id>` : Retrieve a specific item including showing the cart it is in
- `DELETE /ITEMS/<int:id>` : Delete a specific item

### CHECKOUT
- `POST /checkout` : Adds an item to a cart, including its quantity and brand
- `GET /checkout` : Retrieve all the items in carts and their quantities and brands

### ADD_ITEMS

## PROJECT OVERVIEW & FEATURES
- This project should teach me more about association objects
- Every cart should have a specific quantity of items
- Should display the quantity of the item each cart when requesting a specific item

## PROJECT STATUS
- [x] PHASE 1 :CRUD for carts and items
- [x] PHASE 2 :Validator for carts and items
- [x] PHASE 3 :Junction table that connects both 
- [x] PHASE 4 :Implementing association objects
- [] PHASE 5 :Finish project