from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func, select

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

db = SQLAlchemy(app)

class Categories(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    categories = db.Column(db.String(40),unique=True, nullable = False)
    workout = db.relationship('Workouts', backref='category', lazy=True)
    
    def __repr__(self):
        return f'<Added: {self.categories}'
    
    def to_dict(self):
        return {
            'id' : self.id,
            'category' : self.category
        }

class Workouts(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    workouts = db.Column(db.String(80), unique = True, nullable = False)
    rep_set = db.Column(db.String(4),nullable = False)
    status = db.Column(db.String(10), nullable = False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)
    
    
    def __repr__(self):
        return f'<Added: {self.workouts}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'workout': self.workouts,
            'rep_set': self.rep_set,
            'status': self.status,
            'category_id': self.category_id
        }
'''
with app.app_context(): 
    db.create_all()
'''
@app.route('/workouts', methods=['POST', 'GET'])
def add_workout():
    if request.method == 'POST':
        data = request.get_json()
        if 'workouts' not in data or 'rep_set' not in data or 'status' not in data or 'category_id' not in data:
            return {"error": "Missing required fields"}, 400
        if not data['workouts'] or not data['rep_set'] or not data['status'] or not data['category_id']:
            return {"error": "Missing required fields"}, 400
        workout = Workouts(workouts=data['workouts'], rep_set=data['rep_set'], status=data['status'], category_id=data['category_id'])
        db.session.add(workout)
        db.session.commit()
        return workout.to_dict(), 201
    
    if request.method == 'GET':
        workouts = Workouts.query.all()
        workout_list = [workout.to_dict() for workout in workouts]
        return {"Workouts":workout_list}, 200
    
@app.route('/workouts/<int:id>', methods=['PUT', 'GET', 'DELETE'])
def workout_id(id):
    if request.method == 'PUT':
        workout = Workouts.query.filter_by(id=id).first()
        if not workout:
            return {"error": "Content not found"}, 404
        data = request.get_json()
        if 'workouts' not in data or 'rep_set' not in data or 'status' not in data or 'category_id' not in data:
            return {"error": "Missing required fields"}, 400
        if not data['workouts'] or not data['rep_set'] or not data['status'] or not data['category_id']:
            return {"error": "Missing required fields"}, 400
        workout.workouts = data['workouts']
        workout.rep_set = data['rep_set']
        workout.status = data['status']
        workout.category_id = data['category_id']
        db.session.commit()
        return workout.to_dict(), 200

    if request.method == 'GET':
        workout = Workouts.query.filter_by(id=id).first()
        if not workout:
            return {"error": "Content not found"}, 404
        return workout.to_dict(), 200
    
    if request.method == 'DELETE':
        workout = Workouts.query.filter_by(id=id).first()
        if not workout:
            return {"error": "Content not found"}, 404
        db.session.delete(workout)
        db.session.commit()
        return {"message": "Successfully deleted"}, 200
    
if __name__ == '__main__':
    app.run(debug=True)