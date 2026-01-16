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
Todo = [{'Status': None, 'Task': None, 'ID': 0}]

@app.route('/Todo', methods=['GET', 'POST'])
def todo_list():
    if request.method == 'GET':
        return {"To do list:": Todo}, 200
    
    if request.method == 'POST':
        data = request.get_json()
        user_status = data['Status']
        todo_task = data['Task']
        test_status = {'Status': user_status, 'Task': todo_task, 'ID': id_gen()}
        Todo.append(test_status)
        return test_status, 201
    
@app.route('/Todo/<int:id>', methods=['GET', 'PUT', 'DELETE'])     
def task_id(id):
    if request.method == 'GET':
        for task in Todo:
            if task['ID'] == id:
                return task
        return {"Error": "Task not found"}, 404
    
    if request.method == 'PUT':
        for task in Todo:
            if task['ID'] == id:
                data = request.get_json()
                updated_status = data['Status']
                Todo[id]['Status'] = updated_status
                return task, 200
    
    if request.method == 'DELETE':
        for task in Todo:
            if task['ID'] == id:
                Todo.remove(task)
                return f"Successfully removed the task: \n{Todo}", 200
        return {"Error": "Task not found"}, 404
                
def id_gen():
    if not Todo:
        return 1
    else:
        ids = [task['ID'] for task in Todo]
        return max(ids)+1
if __name__ == '__main__':
    app.run(debug=True)