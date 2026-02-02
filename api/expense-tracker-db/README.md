Markdowns to remember: 
'#' For headings 
'-' for bullet points 
'code' for inline code 
'''code block''' for code blocks 
'[x]' for completed checkboxes 
'[]' for incomplete checkboxes

# EXPENSE-TRACKER DATABASE
3rd database conversion of my hardcoded API, an expense tracker that filters your expenses by category and track them, it will also provide the total sum for each category and all the expenses. 

## THINGS TO CONSIDER
- Should have a CRUD for expenses and categories
- Should have a validator
- It should include the expenses for each category, so it should have an ID
- When accessing the category, it should include the expenses then the total of expenses at the end of the list
- 

## FEATURES
- Gets the total sum of the expenses then return it
- Validator detects if the user inputs are invalid
- 

## PROJECT OVERVIEW
- This project will be my last conversion and I will be doing a new project with the usage of database, to solidify my knowledge with the usage of database.

# ENDPOINTS

## CATEGORIES
- '/POST categories : Creates a new category'
- '/GET categories : Retrieves all the category'
- '/PUT<int:id> categories : Updates a specific category'
- '/GET<int:id> categories : Retrieves a specific category'
- '/DELETE<int:id> categories : Delete a specific category'

## EXPENSES
- '/POST/expenses' : Create a new expense
- '/GET/expenses' : Retrieves all the expenses
- '/PUT/expenses/int:id' : Updates a specific expense
- '/GET/expenses/int:id' : Retrieves a specific expense
- '/DELETE/expenses/int:id' : Delete a specific expense

# PROJECT STATUS
- [x] PHASE 1: CRUD for both categories and expenses
- [x] PHASE 2: Validator for both categories and expenses
- [x] PHASE 3: Mapping the categories and expenses
- [] PHASE 4: Getting the sum for each expenses within the category
- [] PHASE 5: 