
def task_id(id):
    for task in Todo:
        if task['id'] == id:
            return task
def id_gen():
    if not Todo:
        return 1
    else:
        ids = [task['id'] for task in Todo]
        return max(ids)+1
    
Todo = [{'Task': None, 'id': 0},{'Task': None, 'id': id_gen()},{'Task': None, 'id': id_gen()},{'Task': None, 'id': id_gen()},{'Task': None, 'id': id_gen()}]

print(id_gen())
