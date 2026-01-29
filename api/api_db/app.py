from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configure the database
# This creates a file called 'test.db' in your current directory
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Create the database object
db = SQLAlchemy(app)

# Define a simple model (like a blueprint for a table)
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(10), nullable=False)
    description = db.Column(db.String(120), nullable=False)
    
    def __repr__(self):
        return f'<Tasks:{self.description}>'

# This is where you'll experiment
if __name__ == '__main__':
    with app.app_context():
        # Create the tables
        db.create_all()
        print("Database tables created!")
        # EXPERIMENT HERE - Try these one at a time:
        
        # 1. Create a new task
        #new_task = Todo(status='Pending', description='Jogging')
        #db.session.add(new_task)
        #db.session.commit()
        #print(f"Added {new_task}")
        
        # 2. Query all tasks
        #tasks = Todo.query.all()
        #print(f"All task: {tasks}")
        
         #2.1 Query for a specific task using their ID and displaying their details such as their status and description (hardcoded style)
        #for task in tasks:
            #if task.id == 1:
                #print(f"ID: {task.id}")
                #print(f"STATUS: {task.status}")
                #print(f"DESCRIPTION: {task.description}")
        
        # 3. Find a task
        #task = Todo.query.filter_by(id=2).first()
        #print(f"Found: {task}")
        #print(f"DESCRIPTION: {task.description}")
        #print(f"STATUS: {task.status}")
        
        # 4. Update a task's status
        task = Todo.query.filter_by(id=1).first()
        task.status = "Completed"
        print(f"Updated task: {task.description}")
        print(f"Current status: {task.status}")
        db.session.commit()
        
        # 5. Delete a task
        #tasks = Todo.query.filter_by(id=1).first()
        #db.session.delete(tasks)
        #db.session.commit()
        #print("Task deleted")
        