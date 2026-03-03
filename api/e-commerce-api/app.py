from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

db = SQLAlchemy(app)

class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(120), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    
    def to_dict(self):
        return {
            "id" : self.id,
            "name" : self.name,
            "description" : self.description,
            "price" : self.price,
            "stock" : self.stock 
        }
class Categories(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    
    def to_dict(self):
        return {
            "id" : self.id,
            "name" : self.name
        }
        
class Orders(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String, nullable=False)
    total = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(50), nullable=False)
    created_date = db.Column(db.DateTime, default=datetime.now)
    
    def to_dict(self):
        return {
            "id" : self.id,
            "customer_name" : self.customer_name,
            "total" : self.total,
            "status" : self.status,
            "created_date" : self.created_date
        }
'''       
class OrderItems(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column('order_id', db.Integer, db.ForeignKey('orders.id'))
    product_id = db.Column('product_id', db.Integer, db.ForeignKey('products.id'))
    quantity = db.Column(db.Integer, nullable=False)
    price_at_purchase = db.Columm(db.Integer, nullable=False)
    
    def to_dict(self):
        return {
            "id" : self.id,
            "order_id" : self.order_id,z
            "product_id" : self.product_id,
            "quantity" : self.quantity,
            "price_at_purchase" : self.price_at_purchase
        }
'''
'''
with app.app_context():
    db.drop_all()
    db.create_all()
'''
@app.route('/products', methods=['POST', 'GET'])
def add_products():
    if request.method == 'POST':
        data = request.get_json()
        if 'name' not in data or 'description' not in data or 'price' not in data or 'stock' not in data:
            return {"error" : "Missing required fields"}, 400
        if not data['name'] or not data['description'] or not data['price'] or not data['stock']:
            return {"error" : "Missing required fields"}, 400
        product = Products(name=data['name'], description=data['description'], price=data['price'], stock=data['stock'])
        db.session.add(product)
        db.session.commit()
        return product.to_dict(), 201
    
    if request.method == 'GET':
        products = Products.query.all()
        product_list = [product.to_dict() for product in products]
        return {"products" : product_list}, 200

@app.route('/products/<int:id>', methods=['PUT', 'GET', 'DELETE'])
def products_id(id):
    if request.method == 'PUT':
        product = Products.query.filter_by(id=id).first()
        if not product:
            return {"error" : "Product not found"}, 404
        data = request.get_json()
        if 'name' not in data or 'description' not in data or 'price' not in data or 'stock' not in data:
            return {"error" : "Missing required fields"}, 400
        if not data['name'] or not data['description'] or not data['price'] or not data['stock']:
            return {"error" : "Missing required fields"}, 400
        product.name = data['name']
        product.description = data['description']
        product.price = data['price']
        product.stock = data['stock']
        db.session.commit()
        return product.to_dict(), 200
    
    if request.method == 'GET':
        product = Products.query.filter_by(id=id).first()
        if not product:
            return {"error" : "Product not found"}, 404
        return {"product" : product.to_dict()}, 200
    
    if request.method == 'DELETE':
        product = Products.query.filter_by(id=id).first()
        if not product:
            return {"error" : "Product not found"}, 404
        db.session.delete(product)
        db.session.commit()
        return {"message" : "Product deleted successfully"}, 200
    
@app.route('/categories', methods=['POST', 'GET'])
def add_category():
    if request.method == 'POST':
        data = request.get_json()
        if 'name' not in data:
            return {"error" : "Missing required fields"}, 400
        if not data['name']:
            return {"error" : "Missing required fields"}, 400
        category = Categories(name=data['name'])
        db.session.add(category)
        db.session.commit()
        return category.to_dict(), 201
    
    if request.method == 'GET':
        categories = Categories.query.all()
        category_list = [category.to_dict() for category in categories]
        return {"categories" : category_list}, 200
    
@app.route('/categories/<int:id>', methods=['PUT', 'GET', 'DELETE'])
def category_id(id):
    if request.method == 'PUT':
        category = Categories.query.filter_by(id=id).first()
        if not category:
            return {"error" : "Category not found"}, 404
        data = request.get_json()
        if 'name' not in data:
            return {"error" : "Missing required fields"}, 400
        if not data['name']:
            return {"error" : "Missing required fields"}, 400
        category.name = data['name']
        db.session.commit()
        return category.to_dict(), 200
    
    if request.method == 'GET':
        category = Categories.query.filter_by(id=id).first()
        if not category:
            return {"error" : "Category not found"}, 404
        return {"category" : category.to_dict()}, 200
    
    if request.method == 'DELETE':
        category = Categories.query.filter_by(id=id).first()
        if not category:
            return {"error" : "Category not found"}, 404
        db.session.delete(category)
        db.session.commit()
        return {"message" : "Category deleted successfully"}, 200
    
@app.route('/orders', methods=['POST', 'GET'])
def add_order():
    if request.method == 'POST':
        data = request.get_json()
        if 'customer_name' not in data or 'total' not in data or 'status' not in data:
            return {"error" : "Missing required fields"}, 400
        if not data['customer_name'] or not data['total'] or not data['status']:
            return {"error" : "MIssing required fields"}, 400
        order = Orders(customer_name=data['customer_name'], total=data['total'], status=data['status'])
        db.session.add(order)
        db.session.commit()
        return order.to_dict(), 201
    
    if request.method == 'GET':
        orders = Orders.query.all()
        order_list = [order.to_dict() for order in orders]
        return {"orders" : order_list}, 200
    
@app.route('/orders/<int:id>', methods=['PUT', 'GET', 'DELETE'])
def order_id(id):
    if request.method == 'PUT':
        order = Orders.query.filter_by(id=id).first()
        if not order:
            return {"error" : "Order not found"}, 404
        data = request.get_json()
        if 'customer_name' not in data or 'total' not in data or 'status' not in data:
            return {"error" : "Missing required fields"}, 400
        if not data['customer_name'] or not data['total'] or not data['status']:
            return {"error" : "MIssing required fields"}, 400
        order.customer_name = data['customer_name']
        order.total = data['total']
        order.status = data['status']
        db.session.commit()
        return order.to_dict(), 200
    
    if request.method == 'GET':
        order = Orders.query.filter_by(id=id).first()
        if not order:
            return {"error" : "Order not found"}, 404
        return {"order" : order.to_dict()}, 200
    
    if request.method == 'DELETE':
        order = Orders.query.filter_by(id=id).first()
        if not order:
            return {"error" : "Order not found"}, 404
        db.session.delete(order)
        db.session.commit()
        return {"message" : "Order deleted successfully"}, 200
if __name__ == '__main__':
    app.run(debug=True)