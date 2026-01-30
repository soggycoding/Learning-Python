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

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        
@app.route('/todo', methods=['GET', 'POST'])
def todo_list():
    if request.method == 'POST':
        data = request.get_json()
        new_task = Todo(status=data['status'], description=data['description'])
        db.session.add(new_task)
        db.session.commit()
        return {
            'id': new_task.id,
            'status': new_task.status,
            'description': new_task.description}, 201
    
    if request.method == 'GET':
        tasks = Todo.query.all()
        task_list = []
        for task in tasks:
            task = {'id': task.id, 'status': task.status, 'description': task.description}
            task_list.append(task)
        return {'tasks': task_list}, 200

    
@app.route('/todo/<int:id>', methods=['GET', 'PUT', 'DELETE'])   
def task_id(id):
    if request.method == 'GET':
        task = Todo.query.filter_by(id=id).first()
        return {
            'id': task.id,
            'status': task.status,
            'description': task.description
        }, 200

    if request.method == 'PUT':
        task = Todo.query.filter_by(id=id).first()
        data = request.get_json()
        task.status = data['status']
        task.description = data['description']
        db.session.commit()
        return {
            'id': id,
            'status': task.status,
            'description': task.description
        }, 200

    if request.method == 'DELETE':
        task = Todo.query.filter_by(id=id).first()
        db.session.delete(task)
        db.session.commit()
        return {"message": "Successfully deleted the task"}, 200
                     


if __name__ == '__main__':
    app.run(debug=True)