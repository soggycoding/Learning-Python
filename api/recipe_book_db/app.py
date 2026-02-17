from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

db = SQLAlchemy(app)

class Ingredients(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ingredient_name = db.Column(db.String(80), nullable=False)
    recipeingredient = db.relationship('RecipeIngredient', back_populates='ingredient',
                                       cascade='all, delete-orphan')

    def __repr__(self):
        return f'<Added {self.ingredient_name}>'
    
    def to_dict(self):
        return {
            'id' : self.id,
            'ingredient' : self.ingredient_name,
        }
    
    def to_dict_with_recipe(self):
        return {
            'id' : self.id,
            'ingredient' : self.ingredient_name,
            'recipes' : [r.to_dict() for r in self.recipeingredient]
        }

class Recipes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    recipe_name = db.Column(db.String(60), nullable=False)
    description = db.Column(db.String(120), nullable=False)
    prep_time = db.Column(db.Integer, nullable=False)
    cook_time = db.Column(db.Integer, nullable=False)
    recipeingredient = db.relationship('RecipeIngredient', back_populates='recipe',
                                       cascade='all, delete-orphan')
    
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
    
    def to_dict_with_ingredient(self):
        return {
            'id': self.id,
            'recipe_name': self.recipe_name,
            'description': self.description,
            'prep_time': self.prep_time,
            'cook_time': self.cook_time,
            'ingredient' : [i.to_dict() for i in self.recipeingredient]
        }
        
class RecipeIngredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ingredient_id = db.Column('ingredient_id', db.Integer, db.ForeignKey('ingredients.id'))
    recipe_id = db.Column('recipe_id', db.Integer, db.ForeignKey('recipes.id'))
    measurement = db.Column(db.String(20), nullable=False)
    
    ingredient = db.relationship('Ingredients', back_populates='recipeingredient')
    recipe = db.relationship('Recipes', back_populates='recipeingredient')
    
    def to_dict(self):
        return {
            'ingredient_id' : self.ingredient_id,
            'recipe_id' : self.recipe_id,
            'ingredient': self.ingredient.ingredient_name,
            'recipe': self.recipe.recipe_name,
            'measurement': self.measurement
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
        if 'ingredient' not in data:
            return {"error": "Missing required fields"}, 400
        if not data['ingredient']:
            return {"error": "Missing required fields"}, 400
        ingredient.ingredient_name = data['ingredient']
        db.session.commit()
        return ingredient.to_dict(), 200
    
    if request.method == 'GET':
        ingredient = Ingredients.query.filter_by(id=id).first()
        if not ingredient:
            return {"error" : "Ingredient not found"}, 404
        recipe_list = [recipe.to_dict() for recipe in ingredient.recipeingredient]
        return {"ingredient": ingredient.to_dict(),
                'recipes': recipe_list}, 200
    
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
        
        ingredient_list = [ingredient.to_dict() for ingredient in recipe.recipeingredient]
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
        
@app.route('/recipe_ingredient', methods=['POST', 'GET'])
def add_ingredient_in_recipe():
    if request.method == 'POST':
        data = request.get_json()
        if 'ingredient_id' not in data or 'recipe_id' not in data or 'measurement' not in data:
            return {"error": "Missing required fields"}, 400
        if not data['ingredient_id'] or not data['recipe_id'] or not data['measurement']:
            return {"error": "Missing required fields"}, 400
        existing = RecipeIngredient.query.filter_by(
            ingredient_id=data['ingredient_id'],
            recipe_id=data['recipe_id']
        ).first()
        
        if existing:
            return {"error": "Ingredients already have measurements"}, 400
        
        recipeingredient = RecipeIngredient(
            ingredient_id=data['ingredient_id'],
            recipe_id=data['recipe_id'],
            measurement=data['measurement']
        )
        db.session.add(recipeingredient)
        db.session.commit()
        
        return recipeingredient.to_dict(), 201
    
    if request.method == 'GET':
        recipeingredient = RecipeIngredient.query.all()
        recipeingredient_list = [r.to_dict() for r in recipeingredient]
        return {"information": recipeingredient_list}, 200
    
@app.route('/recipe_ingredient/<int:id>', methods=['PUT', 'GET', 'DELETE'])
def recipe_ingredient_id(id):
    if request.method == 'PUT':
        recipeingredient = RecipeIngredient.query.filter_by(id=id).first()
        if not recipeingredient:
            return {"error": "RecipeIngredient not found"}, 404
        data = request.get_json()
        if "ingredient_id" not in data or "recipe_id" not in data or "measurement" not in data:
            return {"error": "Missing required fields"}, 400
        if not data['ingredient_id'] or not data['recipe_id'] or not data['measurement']:
            return {"error": "Missing required fields"}, 400
        ingredient = Ingredients.query.get(data['ingredient_id'])
        if not ingredient:
            return {"error" : "Ingredient not found"}, 404
        recipe = Recipes.query.get(data['recipe_id'])
        if not recipe:
            return {"error": "Recipe not found"}, 404
        recipeingredient.ingredient_id = data['ingredient_id']
        recipeingredient.recipe_id = data['recipe_id']
        recipeingredient.measurement = data['measurement']
        db.session.commit()
        return recipeingredient.to_dict(), 200
    
    if request.method == 'GET':
        recipeingredient = RecipeIngredient.query.filter_by(id=id).first()
        if not recipeingredient:
            return {"error": "RecipeIngredient not found"}, 404
        return {"RecipeIngredient": recipeingredient.to_dict()}, 200
    
    if request.method == 'DELETE': 
        recipeingredient = RecipeIngredient.query.filter_by(id=id).first()
        

@app.route('/recipe_ingredient/<int:recipe_id>/ingredient/<int:ingredient_id>', methods=['DELETE'])
def delete_ingredient(recipe_id, ingredient_id):
    ingredient = Ingredients.query.filter_by(id=ingredient_id)
    if not ingredient:
        return {"error": "Ingredient not found"}, 404
    recipe = Recipes.query.filter_by(id=recipe_id)
    if not recipe:
        return {"error": "Recipe not found"}, 404
    ingredient_to_remove = RecipeIngredient.query.filter_by(
        recipe_id=recipe_id,
        ingredient_id=ingredient_id
    ).first()
    
    if not ingredient_to_remove:
        return {"error": "Ingredient not found in recipe"}, 404
    
    db.session.delete(ingredient_to_remove)
    db.session.commit()
    return {"message": "Successfully removed ingredient from recipe"}, 200

if __name__ == '__main__':
    app.run(debug=True)