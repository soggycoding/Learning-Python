Markdowns to remember: 
'#' For headings 
'-' for bullet points 
'code' for inline code 
'''code block''' for code blocks 
'[x]' for completed checkboxes 
'[]' for incomplete checkboxes

# 🍲 Recipe Book Database
- A RESTful API that stores the recipes with the ingredients needed

## 🚀 Getting Started
### Prerequisites
* Python, Flask, SQLAlchemy

### Installation
1. Clone the repo: `git clone ...`
2. Install dependencies: `npm install` (or your equivalent)
3. Set up your `.env` file (Database URLs, API keys)
4. Run migrations/start: `npm start`

## 🛠 Tech Stack
* Flask, Python, SQlalchemy

## 📊 Database Schema
*Optional but highly recommended for a DB project.*
* One recipe has many ingredients
* An ingredient can be found in many recipes
* [Link to an ER Diagram image if you have one]

## 🛣 API Endpoints

### Recipes
- `GET /recipes` - Fetch all recipes
- `POST /recipes` - Create a new recipe
- `PUT /recipes/<int:id>` - Updates a specific recipe
- `GET /recipes/<int:id>` - Get the specific recipe along with the required ingredients
- `DELETE /recipes/<int:id>` - Delete a specific recipe
### Ingredients
- `GET /ingredients` - List all ingredients
- `POST /ingredients` - Create a new ingredient
- `PUT /ingredients/<int:id>` - Updates a specific ingredient
- `GET /ingredients/<int:id>` - Get a specific ingredient and a list of recipes that uses the ingredient
- `DELETE /ingredients/<int:id>` - Delete a specific ingredient


## 📝 Project Overview & Features
* **Feature 1:** Search recipes by ingredient.
* **Feature 2:** Automatic unit conversion (oz to grams).
* **Things to Consider:** Mention any specific logic here.

## 🚦 Project Status
- [x] CRUD for recipe and ingredients
- [x] Validator for recipe and ingredients
- [x] Junction Table
- [ ] Measurements for ingredients