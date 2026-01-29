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
         return f'<id: {self.id}, description: {self.description}>'
task = Todo()

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
        return f"all task: {tasks}", 200
    '''
    if request.method == 'POST':
        data = request.get_json()
        status = data['Status']
        task_description = data['Task']
        new_task = {'Status': status, 'Task': task_description, 'ID': id_gen()}
        todo.append(new_task)
        return new_task, 201

    
@app.route('/todo/<int:id>', methods=['GET', 'PUT', 'DELETE'])

    
def task_id(id):
    if request.method == 'GET':
        for task in todo:
            if task['ID'] == id:
                return task
        return {"error": "Task not found"}, 404
    
    if request.method == 'PUT':
        for task in todo:
            if task['ID'] == id:
                data = request.get_json()
                task['Status'] = data['Status']
                task['Task'] = data['Task']
                return task, 200
        return {"error": "Task not found"}, 404
    if request.method == 'DELETE':
        for task in todo:
            if task['ID'] == id:
                todo.remove(task)
                return {"message": "Successfully removed the task"}, 200
        return {"error": "Task not found"}, 404
                
def id_gen():
    if not todo:
        return 1
    else:
        ids = [task['ID'] for task in todo]
        return max(ids)+1
'''

if __name__ == '__main__':
    app.run(debug=True)