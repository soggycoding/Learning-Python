from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

db = SQLAlchemy(app)

class Company(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    industry = db.Column(db.String(40), nullable=False)
    
    #jobapplication = db.relationship("JobApplication", backref='jobapplication', lazy=True)
    
    def to_dict(self):
        return {
            "name" : self.name,
            "industry" : self.industry
        }

class JobApplication(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    role = db.Column(db.String(20), nullable=False)
    status = db.Column(db.String(20), nullable=False)
    applied_date = db.Column(db.DateTime, default=datetime.now)
    notes = db.Column(db.String(60), nullable=True)
    
    #company = db.relationship('Company', backref='company', lazy=True)
    #interview = db.relationship('Interview', backref='jobapplication', lazy=True)
    
    def to_dict(self):
        return {
            "role" : self.role,
            "status" : self.status,
            "applied_date" : self.applied_date,
            "notes" : self.notes
        }
        
class Interview(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    round = db.Column(db.Integer(), nullable=False)
    scheduled_date = db.Column(db.String(40), nullable=False)
    outcome = db.Column(db.String(20), nullable=False)
    
    #jobapplication = db.relationship('JobApplication', backref='interview', lazy=True)
    
    
    def to_dict(self):
        return {
            "round" : self.round,
            "scheduled_date" : self.scheduled_date,
            "outscome" : self.outcome
        }
    '''    
    with app.app_context():
        db.drop_all()
        db.create_all()  
    '''
@app.route ('/company', methods=['POST', 'GET'])
def add_company():
    if request.method == "POST":
        data = request.get_json()
        if 'name' not in data or 'industry' not in data:
            return {"error" : "Missing required fields"}, 400
        if not data['name'] or not data['industry']:
            return {"error" : "Missing required fields"}, 400
        company = Company(name=data['name'], industry=data['industry'])
        db.session.add(company)
        db.session.commit()
        return company.to_dict(), 201
    
    if request.method == "GET":
        companies = Company.query.all()
        company_list = [company.to_dict() for company in companies]
        return {
            "companies" : company_list
        }

@app.route ('/company/<int:id>', methods=['PUT', 'GET', 'DELETE'])
def update_company(id):
    if request.method == "PUT":
        company = Company.query.filter_by(id=id).first()
        if not company:
            return {"error" : "Company not found"}, 404
        data = request.get_json()
        if 'name' not in data or 'industry' not in data:
            return {"error" : "Missing required fields"}, 400
        if not data['name'] or not data['industry']:
            return {"error" : "Missing required fields"}, 400
        company.name = data['name']
        company.industry = data['industry']
        db.session.commit()
        return company.to_dict(), 200
    
    if request.method == "GET":
        company = Company.query.filter_by(id=id).first()
        if not company:
            return {"error" : "Company not found"}, 404
        return {
            "Company " : company.to_dict()
        }, 200
        
    if request.method == "DELETE":
        company = Company.query.filter_by(id=id).first()
        if not company:
            return {"error" : "Company not found"}, 404
        db.session.delete(company)
        db.session.commit()
        return {"message": "Company deleted successfully"}, 200
if __name__ == '__main__':
    app.run(debug=True)