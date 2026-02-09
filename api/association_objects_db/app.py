from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

db = SQLAlchemy(app)
CartsItems = db.Table('CartsItems',
                      db.Column('item_id', db.Integer, db.ForeignKey('items.id')),
                                db.Column('cart_id', db.Integer, db.ForeignKey('carts.id')))
              
class Items(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(80), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    cart = db.relationship('Carts', secondary=CartsItems, backref=db.backref('item', lazy='dynamic'))
    
    def __repr__(self):
        return f'<Added {self.item_name}>'
        
    def to_dict(self):
        return {
            'id' : self.id,
            'item' : self.item_name,
            'quantity' : self.quantity
        }

class Carts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cart_user = db.Column(db.Integer, primary_key=True)
    
    def __repr__(self):
        return f"<Added {self.cart_user}>"
    
    def to_dict(self):
        return {
            'id' : self.id,
            'cart_user' : self.cart_user
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
        if 'item' not in data or 'quantity' not in data:
            return {"error": "Missing required fields"}, 400
        if not data['item'] or not data['quantity']:
            return {"error": "Missing required fields"}, 400
        item = Items(item_name=data['item'], quantity=data['quantity'])
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
        if 'item' not in data or 'quantity' not in data:
            return {"error" : "Missing required fields"}, 400
        if not data['item'] or not data['quantity']:
            return {"error" : "Missing required fields"}, 400
        item.item_name = data['item']
        item.quantity = data['quantity']
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

@app.route('/carts/<int:cart_id>/item', methods=['POST'])
def add_item_to_cart(cart_id):
    cart = Carts.query.get(cart_id)
    if not cart:
        return {"error": "Cart not found"}, 404
    
    data = request.get_json()
    if 'item_id' not in data:
        return {"error" : "Missing required fields"}, 400
    if not data['item_id']:
        return {"error" : "Missing required fields"}, 400
    item_id= data['item_id']
    
    item = Items.query.get(item_id)
    if not item:
        return {"error" : "Item not found"}, 404
    if item in cart.item:
        return {"message" : "Item already in cart"}, 200
    
    cart.item.append(item)
    db.session.commit()
    
    return {
        'cart': cart.to_dict(),
        'item_added': item.to_dict()
    }, 201
if __name__ == '__main__':
    app.run(debug=True)