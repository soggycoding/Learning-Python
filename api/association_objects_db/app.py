from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

db = SQLAlchemy(app)
#checkout = db.Table('checkout', 
#                      db.Column('item_id', db.Integer, db.ForeignKey('items.id')), 
#                      db.Column('cart_id', db.Integer, db.ForeignKey('carts.id')))

class Items(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(80), nullable=False)
    checkout = db.relationship('Checkout', back_populates='item',
                                 cascade='all, delete-orphan')
    
    def __repr__(self):
        return f'<Added {self.item_name}>'
        
    def to_dict(self):
        return {
            'id' : self.id,
            'item' : self.item_name,
        }
    
    def to_dict_with_carts(self):
        return {
            'id' : self.id,
            'name' : self.item_name,
            'cart' : [c.to_dict() for c in self.checkout]
        }

class Carts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cart_user = db.Column(db.String(60), nullable=False)
    checkout = db.relationship('Checkout', back_populates='cart',
                                 cascade='all, delete-orphan')
    
    
    def __repr__(self):
        return f"<Added {self.cart_user}>"
    
    def to_dict(self):
        return {
            'id' : self.id,
            'cart_user' : self.cart_user
        }
    
    def to_dict_with_items(self):
        return {
            'id' : self.id,
            'user' : self.cart_user,
            'item' : [i.to_dict() for i in self.checkout]
        }
        
class Checkout(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column('item_id', db.Integer, db.ForeignKey('items.id'))
    cart_id = db.Column('cart_id', db.Integer, db.ForeignKey('carts.id'))
    quantity = db.Column(db.Integer, nullable=False)
    brand = db.Column(db.String(80), nullable=False)
    
    item = db.relationship('Items', back_populates='checkout')
    cart = db.relationship('Carts', back_populates='checkout')
    
    def to_dict(self):
        return {
            'item_id' : self.item_id,
            'cart_id' : self.cart_id,
            'item' : self.item.item_name,
            'user' : self.cart.cart_user,
            'quantity' : self.quantity,
            'brand' : self.brand
        }
'''
with app.app_context():
    db.drop_all()
    db.create_all()
'''
@app.route('/items', methods=['POST', 'GET'])
def add_items():
    if request.method == 'POST':
        data = request.get_json()
        if 'item' not in data:
            return {"error": "Missing required fields"}, 400
        if not data['item']:
            return {"error": "Missing required fields"}, 400
        item = Items(item_name=data['item'])
        db.session.add(item)
        db.session.commit()
        return item.to_dict(), 201

    if request.method == 'GET':
         items = Items.query.all()
         item_list = [item.to_dict() for item in items]
         return {"items": item_list}, 201
     
@app.route('/items/<int:id>', methods=['PUT', 'GET', 'DELETE'])
def item_id(id):
    if request.method == 'PUT':
        item = Items.query.filter_by(id=id).first()
        if not item:
            return {"error": "Item not found"}, 404
        data = request.get_json()
        if 'item' not in data:
            return {"error" : "Missing required fields"}, 400
        if not data['item']:
            return {"error" : "Missing required fields"}, 400
        item.item_name = data['item']
        db.session.commit()
        return item.to_dict(), 200
    
    if request.method == 'GET':
        item = Items.query.filter_by(id=id).first()
        if not item:
            return {"error": "Item not found"}, 404
        cart_list = [cart.to_dict() for cart in item.cart]
        return {
            'cart' : cart_list,
            'item' : item.to_dict()
        }, 200
    
    if request.method == 'DELETE':
        item = Items.query.filter_by(id=id).first()
        if not item:
            return {"error" : "Item not found"}, 404
        db.session.delete(item)
        db.session.commit()
        return {"message": "Successfully deleted item"}, 200

@app.route('/carts', methods=['POST', 'GET'])
def add_carts():
    if request.method == 'POST':
        data = request.get_json()
        if 'cart_user' not in data:
            return {"error": "Missing required fields"}, 400
        if not data['cart_user']:
            return {"error": "Missing required fields"}, 400
        cart = Carts(cart_user=data['cart_user'])
        db.session.add(cart)
        db.session.commit()
        return cart.to_dict(), 201
    
    if request.method == 'GET':
        carts = Carts.query.all()
        cart_list = [cart.to_dict() for cart in carts]
        return {"carts": cart_list}, 200

@app.route('/checkout', methods=['POST', 'GET'])
def check_items_in_cart():
    if request.method == 'POST':
        data = request.get_json()
        if 'item_id' not in data or 'cart_id' not in data:
            return {"error": "Missing required fields"}, 400
        if not data['item_id'] or not data['cart_id']:
            return {"error": "Missing required fields"}, 400
        item = Items.query.get_or_404(data['item_id'])
        cart = Carts.query.get_or_404(data['cart_id'])
        existing = Checkout.query.filter_by(
            item_id=data['item_id'],
            cart_id=data['cart_id']
        ).first()
        
        if existing:
            return {"error": "Checkout already exists"}, 400
        
        checkout = Checkout(
            item_id=data['item_id'],
            cart_id=data['cart_id'],
            quantity=data.get('quantity'),
            brand=data.get('brand')
        )
        db.session.add(checkout)
        db.session.commit()
        
        return checkout.to_dict(), 201
    
    if request.method == 'GET':
        checkout = Checkout.query.all()
        checkout_list = [check.to_dict() for check in checkout]
        return {"checkout": checkout_list}, 200
    
@app.route('/checkout/<int:id>', methods=['PUT', 'GET', 'DELETE'])
def checkout_id(id):
    if request.method == 'PUT':
        
if __name__ == '__main__':
    app.run(debug=True)