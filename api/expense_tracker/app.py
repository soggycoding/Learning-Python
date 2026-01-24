#EXPENSE TRACKER
from flask import Flask, request

app = Flask(__name__)
categories = []
expenses = []
@app.route('/categories', methods=['POST', 'GET'])
def expense_category():
    if request.method == 'POST':
        data = request.get_json()
        if 'category' not in data:
            return {"error": "Missing required fields"}, 400
        expense_category = data['category']
        if not expense_category:
            return {"error": "Missing required fields"}, 400
        category = {'id': category_id_gen(), 'category': expense_category}
        categories.append(category)
        return category, 201
    
    if request.method == 'GET':
        return {'categories':categories}, 200
    
@app.route('/categories/<int:id>', methods=['PUT', 'GET', 'DELETE'])
def get_category_by_id(id):
    if request.method == 'PUT':
        for category in categories:
            if category['id'] == id:
                data = request.get_json()
                category['category'] = data['category']
                return category, 200
        return {"error": "Content not found"}, 404
    if request.method == 'GET':
        for category in categories:
            if category['id'] == id:
                return category, 200
        return {"error": "Content not found"}, 404
    if request.method == 'DELETE':
        for category in categories:
            if category['id'] == id:
                categories.remove(category)
                return{"message": "Successfully deleted"}, 200
        return {"error": "Content not found"}, 404
@app.route('/expenses', methods=['POST', 'GET'])
def user_expense():
    if request.method == 'POST':
        data = request.get_json()
        if 'description' not in data or 'cost' not in data or 'date' not in data or 'category_id' not in data:
            return {'error': 'Missing required fields'}, 400
        description = data['description']
        cost = data['cost']
        date = data['date']
        category_id = data['category_id']
        if not description or not cost or not date or not category_id:
            return {'error': 'Missing required fields'}, 400 
        expense = {'id': expenses_id(), 'description': description, 'cost': cost, 'date': date, 'category_id': category_id}
        for category in categories:
            if category['id'] == category_id:
                expenses.append(expense)
                return expense, 201
        return {"error": "Content not found"}, 404
    
    if request.method == 'GET':
        return {'expenses': expenses}, 200
@app.route('/expenses/<int:id>', methods=['PUT', 'GET', 'DELETE'])
def expense_id(id):
    if request.method == 'GET':
        for expense in expenses:
            if expense['id'] == id:
                expense_id = expense
                break

    if expense_id:
        for category in categories:
            if expense_id['category_id'] == category['id']:
                return [expense_id,category], 200
    else:
        return {"error": "Content not found"}, 404
            
    if request.method == 'PUT':
        for expense in expenses:
            if expense['id'] == id:
                data = request.get_json()
                if 'description' not in data or 'cost' not in data or 'date' not in data or 'category_id' not in data:
                    return {'error': 'Missing required fields'}, 400
                expense['description'] = data['description']
                expense['cost'] = data['cost']
                expense['date'] = data['date']
                expense['category_id'] = data['category_id']
                for category in categories:
                    if category['id'] == expense['category_id']:
                        return expense, 200
        return {"error": "Content not found"}, 404
    
    if request.method == 'DELETE':
        for expense in expenses:
            if expense['id'] == id:
                expenses.remove(expense)
                return {"message":"Expense removed successfully"}, 200
        return{"error": "Content not found"}, 404
def category_id_gen():
    if not categories:
        return 1
    else:
        ids = [category['id'] for category in categories]
        return max(ids)+1
def expenses_id():
    if not expenses:
        return 1
    else: 
        ids = [expense['id'] for expense in expenses]
        return max(ids)+1
if __name__ == '__main__':
    app.run(debug=True)