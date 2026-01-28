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
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    
    def __repr__(self):
        return f'<User {self.name}>'

# This is where you'll experiment
if __name__ == '__main__':
    with app.app_context():
        # Create the tables
        db.create_all()
        print("Database tables created!")
        # EXPERIMENT HERE - Try these one at a time:
        
        # 1. Create a new user
        new_user = User(name='Bingbing', email='balingbing@gmail.com')
        db.session.add(new_user)
        db.session.commit()
        print(f"Created: {new_user}")
        
        # 2. Query all users
        users = User.query.all()
        #emails = User.query.get(id)
        print(f"All users: {users}")
        #print(f"All emails: {emails}")
        
        # 3. Find a specific user
        #user = User.query.filter_by(name='Bingbing').first()
        #print(f"Found: {user}")
        
        # 4. Update a user
        #user = User.query.filter_by(name='Bingbong').first()
        #user.email = 'Bingbong@gmail.com'
        #db.session.commit()
        #print(f"Updated: {user}")ss
        
        # 5. Delete a user
        user = User.query.filter_by(name='Bingbing').first()
        db.session.delete(user)
        db.session.commit()
        print("User deleted")