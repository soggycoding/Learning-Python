from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

db = SQLAlchemy(app)

IngredientRecipe = db.Table('IngredientRecipe',
                            db.Column('ingredient_id', db.Integer, db.ForeignKey('ingredients.id')),
                            db.Column('recipe_id', db.Integer, db.ForeignKey('recipes.id'))
                            )
class Ingredients(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ingredient_name = db.Column(db.String(80), nullable=False)
    recipe = db.relationship('Recipes', secondary=IngredientRecipe, backref=db.backref('ingredient', lazy='dynamic'))
    
    def __repr__(self):
        return f'<Added {self.ingredient_name}>'
    
    def to_dict(self):
        return {
            'id' : self.id,
            'ingredient' : self.ingredient_name,
        }

class Recipes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    recipe_name = db.Column(db.String(60), nullable=False)
    description = db.Column(db.String(120), nullable=False)
    prep_time = db.Column(db.Integer, nullable=False)
    cook_time = db.Column(db.Integer, nullable=False)
    
    def __repr__(self):
        return f'<Added {self.recipe_name}>'
    
    def to_dict(self):
        return {
            'id' : self.id,
            'recipe_name' : self.recipe_name,
            'description' : self.description,
            'prep_time' : self.prep_time,
            'cook_time' : self.cook_time
        }
'''       
with app.app_context():
    db.drop_all()
    db.create_all()
'''
@app.route('/ingredients', methods=['POST', 'GET'])
def add_ingredients():
    if request.method == 'POST':
        data = request.get_json()
        if 'ingredient' not in data:
            return {"error": "Missing required fields"}, 400
        if not data['ingredient']:
            return {"error": "Missing required fields"}, 400
        ingredients = Ingredients(ingredient_name=data['ingredient'])
        db.session.add(ingredients)
        db.session.commit()
        return ingredients.to_dict(), 201

    if request.method == 'GET':
        ingredients = Ingredients.query.all()
        ingredient_list = [ingredient.to_dict() for ingredient in ingredients]
        return {"ingredients": ingredient_list}, 200

@app.route('/ingredients/<int:id>', methods=['PUT', 'GET', 'DELETE'])
def ingredient_id(id):
    if request.method == 'PUT':
        ingredient = Ingredients.query.filter_by(id=id).first()
        if not ingredient:
            return {"error": "Ingredient not found"}, 404
        data = request.get_json()
        if 'ingredient' not in data or 'measurement' not in data:
            return {"error": "Missing required fields"}, 400
        if not data['ingredient'] or not data['measurement']:
            return {"error": "Missing required fields"}, 400
        ingredient.ingredient_name = data['ingredient']
        db.session.commit()
        return ingredient.to_dict(), 200
    
    if request.method == 'GET':
        ingredient = Ingredients.query.filter_by(id=id).first()
        if not ingredient:
            return {"error" : "Ingredient not found"}, 404
        return {"ingredient": ingredient.to_dict()}, 200
    
    if request.method == 'DELETE':
        ingredient = Ingredients.query.filter_by(id=id).first()
        if not ingredient:
            return {"error" : "Ingredient not found"}, 404
        db.session.delete(ingredient)
        db.session.commit()
        return {"message": "Successfully deleted"}, 200
    
@app.route('/recipes', methods=['POST', 'GET'])
def add_recipe():
    if request.method == 'POST':
        data = request.get_json()
        if 'recipe_name' not in data or 'description' not in data or 'prep_time' not in data or 'cook_time' not in data:
            return {"error": "Missing required fields"}, 400
        if not data['recipe_name'] or not data['description'] or not data['prep_time'] or not data['cook_time']:
            return {"error": "Missing required fields"}, 400
        recipe = Recipes(recipe_name=data['recipe_name'], description=data['description'], prep_time=data['prep_time'], cook_time=data['cook_time'])
        db.session.add(recipe)
        db.session.commit()
        return recipe.to_dict(), 201
    
    if request.method == 'GET':
        recipes = Recipes.query.all()
        recipe_list = [recipe.to_dict() for recipe in recipes]
        return {"recipes": recipe_list}, 200

@app.route('/recipes/<int:id>', methods=['PUT', 'GET', 'DELETE'])
def recipe_id(id):
    if request.method == 'PUT':
        recipe = Recipes.query.filter_by(id=id).first()
        if not recipe:
            return {"error": "Content not found"}, 404
        data = request.get_json()
        if 'recipe_name' not in data or 'description' not in data or 'prep_time' not in data or 'cook_time' not in data:
            return {"error": "Missing required fields"}, 400
        if not data['recipe_name'] or not data['description'] or not data['prep_time'] or not data['cook_time']:
            return {"error": "Missing required fields"}, 400
        recipe.recipe_name = data['recipe_name']
        recipe.description = data['description']
        recipe.prep_time = data['prep_time']
        recipe.cook_time = data['cook_time']
        db.session.commit()
        return recipe.to_dict(), 200
    
    if request.method == 'GET':
        recipe = Recipes.query.filter_by(id=id).first()
        if not recipe:
            return {"error": "Content not found"}, 404
        
        ingredient_list = [ingredient.to_dict() for ingredient in recipe.ingredient]
        return {
            "ingredient": ingredient_list,
            "recipe": recipe.to_dict(),
            }, 200
        
    if request.method == 'DELETE':
        recipe = Recipes.query.filter_by(id=id).first()
        if not recipe:
            return {"error": "Content not found"}, 404
        db.session.delete(recipe)
        db.session.commit()
        return {"message": "Successfully deleted"}, 200
        
@app.route('/recipes/<int:recipe_id>/ingredients', methods=['POST'])
def add_ingredients_to_recipe(recipe_id):
    recipe = Recipes.query.get(recipe_id)
    if not recipe:
        return {"error": "Recipe not found"}, 404
    
    data = request.get_json()
    if 'ingredient_id' not in data:
        return {"error" : "Missing required fields"}, 400
    if not data['ingredient_id']:
        return {"error" : "Missing required fields"}, 400
    ingredient_id = data['ingredient_id']
    
    ingredient = Ingredients.query.get(ingredient_id)
    if not ingredient:
        return {"error" : "Ingredient not found"}, 404
    if ingredient in recipe.ingredient:
        return {"message" : "Ingredient already in recipe"}, 200
    
    recipe.ingredient.append(ingredient)
    db.session.commit()
    
    return {
        'recipe': recipe.to_dict(),
        'ingredient_added' : ingredient.to_dict()
    }, 201
    
if __name__ == '__main__':
    app.run(debug=True)