#EXPENSE TRACKER
from flask import Flask, request

app = Flask(__name__)
categories = []
@app.route('/category', methods=['POST', 'GET'])
def expense_category():
    if request.method == 'POST':
        data = request.get_json()
        expense_category = data['']
        if expense_category == '':
            return {"error": "Missing required fields"}, 400
        category = {'id': category_id(), 'category': expense_category}
        categories.append(category)
        return category, 201
    
    if request.method == 'GET':
        return categories, 200
@app.route('/category/<int:id>', methods=['PUT', 'GET', 'DELETE'])
def category(id):
    if request.method == 'PUT':
        for category in categories:
            if category['id'] == id:
                data = request.get_json()
                category['category'] = data['']
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
@app.route('/expense', methods=['POST', 'GET'])
def expenses():
    if request.method == 'POST':
        data = request.get_json()
def category_id():
    if not categories:
        return 1
    else:
        ids = [category['id'] for category in categories]
        return max(ids)+1
if __name__ == '__main__':
    app.run(debug=True)