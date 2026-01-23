Markdowns to remember:
'#' For headings
'-' for bullet points
'code' for inline code
'''code block''' for code blocks
'[x]' for completed checkboxes
'[]' for incomplete checkboxes

# Expense Tracker API

My 4th project for hardcoded API to prepare for learning DB. It is an  expense tracker that has categories for different types of expenses. You can get the total for everything and you can also get the total for a specific category.

## Things to consider:

- Should be filtered by category
- it should sum all the expenses
- it should also sum all of the expenses for specific category

## Project overview:

With this project, it should help me with:
- Fundamentals of CRUD, and API
- Build a solid foundation for API's and how it works
- Build confidence in coding and give me a better understanding for planning

## ENDPOINTS:

### CATEGORIES:
- `POST /category`Creates a new category
- `GET /category` Retrieves all the category
- `UPDATE /category/<int:id>` Update a specific category
- `GET /category/<int:id>` Retrieves a specific category
- `DELETE /category/<int:id>`Deletes a specific category

### EXPENSES:
- `POST /expenses` Create a new expense
- `GET /expenses` Retrieves all the expenses
- `UPDATE /expenses/<int:id>` Update a specific expense
- `GET /expenses/<int:id>` Retrieve a specific expense
- `DELETE /expenses/<int:id>` Delete a specific expense

## PROJECT STATUS:

- [x] Phase 1: Categories in CRUD
- [x] Phase 2: Expenses CRUD with validation
- [] Phase 3: Enhanced responses with full category details