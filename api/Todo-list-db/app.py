from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Todo(db.Model):
     id = db.Column(db.Integer, primary_key=True)
     status = db.Column(db.String(10), nullable = False)
     description = db.Column(db.String(80), nullable = False)
     
     def __repr__(self):
         return f'<id={self.id}, status={self.status}, description={self.description}>'
     
     def to_dict(self):
         return {
             'id': self.id,
             'status': self.status,
             'description': self.description
         }
if __name__ == '__main__':
    with app.app_context():
        db.create_all() #Run it once to manually create tables
        
@app.route('/todos', methods=['GET', 'POST'])
def todo_list():
    if request.method == 'POST':
        data = request.get_json()
        if 'status' not in data or 'description' not in data:
            return {"error": "Missing required fields"}, 400
        if not data['status'] or not data['description']:
            return {"error": "Missing required fields"}, 400
        new_task = Todo(status=data['status'], description=data['description'])
        db.session.add(new_task)
        db.session.commit()
        return new_task.to_dict(), 201
    
    if request.method == 'GET':
        tasks = Todo.query.all()
        task_list = [task.to_dict() for task in tasks]
        return {'tasks': task_list}, 200

    
@app.route('/todos/<int:id>', methods=['GET', 'PUT', 'DELETE'])   
def task_id(id):
    if request.method == 'GET':
        task = Todo.query.filter_by(id=id).first()
        if not task:
            return {"error": "Task not found"}, 404
        return task.to_dict(), 200

    if request.method == 'PUT':
        task = Todo.query.filter_by(id=id).first()
        if not task:
            return {"error": "Task not found"}, 404
        data = request.get_json()
        if 'status' not in data or 'description' not in data:
            return {"error": "Missing required fields"}, 400
        if not data['status'] or not data['description']:
            return {"error": "Missing required fields"}, 400
        task.status = data['status']
        task.description = data['description']
        db.session.commit()
        return task.to_dict(), 200

    if request.method == 'DELETE':
        task = Todo.query.filter_by(id=id).first()
        if not task:
            return {"error": "Task not found"}, 404
        db.session.delete(task)
        db.session.commit()
        return {"message": "Successfully deleted the task"}, 200
                     
if __name__ == '__main__':
    app.run(debug=True) 