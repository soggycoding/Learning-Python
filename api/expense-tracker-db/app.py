from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func, select

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFITION'] = False

db = SQLAlchemy(app)

class Categories(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(80), unique=True, nullable=False)
    expenses = db.relationship('Expenses', backref='category', lazy=True)
    
    def __repr__(self):
        return f'<Added: {self.category}'
    
    def to_dict(self):
        return {
                'id': self.id,
                'category': self.category
            }
        
class Expenses(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(80), unique=True, nullable=False)
    cost = db.Column(db.Integer, nullable=False)
    date = db.Column(db.String(30), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)
    
    def __repr__(self):
        return f'<Added: {self.description}'
    
    def to_dict(self, show_category=True):
        data = {
            'id': self.id,
            'description': self.description,
            'cost': self.cost,
            'date': self.date,
            'category_id': self.category_id
            }
        if show_category:
            data['category'] = {"category":self.category.category}
            
        return data
        
@app.route('/categories', methods=['POST', 'GET'])
def post_category():
    if request.method == 'POST':
        data = request.get_json()
        if 'category' not in data:
            return {"error": "Missing required fields"}, 400
        if not data['category']:
            return {"error": "Missing required fields"}, 400
        new_category = Categories(category=data['category'])
        db.session.add(new_category)
        db.session.commit()
        return new_category.to_dict(), 201
    
    if request.method == 'GET': 
        categories = Categories.query.all()
        category_list = [category.to_dict() for category in categories]
        return {"categories": category_list}, 200

@app.route('/categories/<int:id>', methods=['PUT', 'GET', 'DELETE'])
def category_id(id):
    if request.method == 'PUT':
        categories = Categories.query.filter_by(id=id).first()
        if not categories:
            return {"error": "Content not found"}, 404
        data = request.get_json()
        if 'category' not in data:
            return {"error": "Missing required fields"}, 400
        if not data['category']:
            return {"error": "Missing required fields"}, 400
        categories.category = data['category']
        db.session.commit()
        return categories.to_dict(), 200

    if request.method == 'GET':
        categories = Categories.query.filter_by(id=id).first()
        if not categories:
            return {"error": "Content not found"}, 404
        return categories.to_dict(), 200
    
    if request.method == 'DELETE':
        categories = Categories.query.filter_by(id=id).first()
        if not categories:
            return {"error": "Content not found"}, 404
        db.session.delete(categories)
        db.session.commit()
        return {"message": "Successfully deleted"}, 200

@app.route('/expenses', methods=['POST', 'GET'])
def post_expense():
    if request.method == 'POST':
        data = request.get_json()
        if 'description' not in data or 'cost' not in data or 'date' not in data or 'category_id' not in data:
            return {"error": "Missing required fields"}, 400
        if not data['description'] or not data['cost'] or not data['date'] or not data['category_id']:
            return {"error": "Missing required fields"}, 400
        category = Categories.query.get(data['category_id'])
        if not category:
            return {"error": "Category not found"}, 404
        new_expense = Expenses(description=data['description'],cost=data['cost'], date=data['date'], category_id=data['category_id'])
        db.session.add(new_expense)
        db.session.commit()
        return new_expense.to_dict(show_category=False), 201
    
    if request.method == 'GET':
        expenses = Expenses.query.all()
        expense_list = [expense.to_dict(show_category = False) for expense in expenses]
        return {"expenses": expense_list}, 200

@app.route('/expenses/<int:id>', methods=['PUT', 'GET', 'DELETE'])
def expense_id(id):
    if request.method == 'PUT':
        expenses = Expenses.query.filter_by(id=id).first()
        if not expenses:
            return {"error": "Content not found"}, 404
        data = request.get_json()
        if 'description' not in data or 'cost' not in data or 'date' not in data or 'category_id' not in data:
            return {"error": "Missing required fields"}, 400
        if not data['description'] or not data['cost'] or not data['date'] or not data['category_id']:
            return {"error": "Missing required fields"}, 400
        expenses.description = data['description']
        expenses.cost = data['cost']
        expenses.date = data['date']
        expenses.category_id = data['category_id']
        db.session.commit()
        return expenses.to_dict(show_category=False), 200

    if request.method == 'GET':
        expenses = Expenses.query.filter_by(id=id).first()
        if not expenses:
            return {"error": "Content not found"}, 404
        return expenses.to_dict(), 200
    
    if request.method == 'DELETE':
        expenses = Expenses.query.filter_by(id=id).first()
        if not expenses:
            return {"error": "Content not found"}, 404
        db.session.delete(expenses)
        db.session.commit()
        return {"message": "Successfully deleted"}, 200

@app.route('/expenses/total', methods=['GET'])
def expenses_total():
    category_id = request.args.get('category_id')
    if not category_id:
        return {"error": "Content not found"}, 404
    if category_id:
        total = db.session.query(func.sum(Expenses.cost)).filter(Expenses.category_id == category_id)
        result = db.session.execute(total).scalar()
        return {"total":result or 0}, 200
    else:
        total = db.session.query(func.sum(Expenses.cost)).scalar()
        return {"total":total or}, 200
    
''' 
with app.app_context():
    db.drop_all()
    db.create_all()
'''
if __name__ == '__main__':
    app.run(debug=True)