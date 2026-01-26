from flask import Flask, request

app = Flask(__name__)
expenses = [{'category_id': 1, 'cost': 150, 'description': 'test', 'id': 1}, {'category_id': 1, 'cost': 200, 'description': 'test2', 'id': 2}, {'category_id': 1, 'cost': 250, 'description': 'test3', 'id': 3}]
@app.route('/test', methods=['GET'])
def test_params():
    category_id = request.args.get('category_id')
    
    if category_id is not None:
        int_category_id = int(category_id)
    else: 
        return{"error": "Content not found"}, 404
    total_sum = 0
    for expense in expenses:
        if expense['category_id'] == int_category_id:
            total_sum += expense['cost']
    return {'total':total_sum}
if __name__ == '__main__':
    app.run(debug=True)