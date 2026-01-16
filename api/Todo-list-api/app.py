#2nd project to do list API
'''
I need a list where I can add, update, delete something, for example a task.
How I will add - using 'POST' in the main HTTP which is /To-do-list
How I will update - using a unique ID generator and assigning them to each task, Identifying them with 'PUT'
How I will delete - using 'delete' to remove something from the list completely
All this will be hardcoded first since it is my second project. 
use CRUD principle.
It should also have a pending or complete on the update and on the main list where it shows everything.
'''
from flask import Flask, request

app = Flask(__name__)
todo = []

@app.route('/todo', methods=['GET', 'POST'])
def todo_list():
    if request.method == 'GET':
        return {"To do list:": todo}, 200
    
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
if __name__ == '__main__':
    app.run(debug=True)