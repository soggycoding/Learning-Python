from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func, select
from datetime import datetime

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False

db = SQLAlchemy(app)

class Companies(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    industry = db.Column(db.String(40), nullable=False)
    
    jobapplication = db.relationship("JobApplications", backref='company', lazy=True)
    
    def to_dict(self):
        return {
            "name" : self.name,
            "industry" : self.industry
        }

class JobApplications(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    role = db.Column(db.String(20), nullable=False)
    status = db.Column(db.String(20), nullable=False)
    applied_date = db.Column(db.DateTime, default=datetime.now)
    notes = db.Column(db.String(60), nullable=True)
    
    company_id = db.Column(db.Integer, db.ForeignKey('companies.id'), nullable=False)
    interview_id = db.Column(db.Integer, db.ForeignKey('interviews.id'), nullable=False)
    
    def to_dict(self):
        return {
            "role" : self.role,
            "status" : self.status,
            "applied_date" : self.applied_date,
            "notes" : self.notes
        }
        
class Interviews(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    round = db.Column(db.Integer(), nullable=False)
    scheduled_date = db.Column(db.String(40), nullable=False)
    outcome = db.Column(db.String(20), nullable=False)
    
    jobapplication = db.relationship('JobApplications', backref='interview', lazy=True)
    
    
    def to_dict(self):
        return {
            "round" : self.round,
            "scheduled_date" : self.scheduled_date,
            "outcome" : self.outcome
        }
    
    def to_dict_with_jobapplication(self):
        return {
            "round" : self.round,
            "scheduled_date" : self.scheduled_date,
            "outcome" : self.outcome,
            "jobapplication" : [j.to_dict() for j in self.jobapplication]
        }
  
with app.app_context():
    db.drop_all()
    db.create_all()  
   
@app.route ('/companies', methods=['POST', 'GET'])
def add_company():
    if request.method == "POST":
        data = request.get_json()
        if 'name' not in data or 'industry' not in data:
            return {"error" : "Missing required fields"}, 400
        if not data['name'] or not data['industry']:
            return {"error" : "Missing required fields"}, 400
        company = Companies(name=data['name'], industry=data['industry'])
        db.session.add(company)
        db.session.commit()
        return company.to_dict(), 201
    
    if request.method == "GET":
        companies = Companies.query.all()
        company_list = [company.to_dict() for company in companies]
        return {
            "companies" : company_list
        }, 200

@app.route ('/companies/<int:id>', methods=['PUT', 'GET', 'DELETE'])
def update_company(id):
    if request.method == "PUT":
        company = Companies.query.filter_by(id=id).first()
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
        company = Companies.query.filter_by(id=id).first()
        if not company:
            return {"error" : "Company not found"}, 404
        return {
            "Company " : company.to_dict()
        }, 200
        
    if request.method == "DELETE":
        company = Companies.query.filter_by(id=id).first()
        if not company:
            return {"error" : "Company not found"}, 404
        db.session.delete(company)
        db.session.commit()
        return {"message": "Company deleted successfully"}, 200
    
@app.route ('/interviews', methods=['POST', 'GET'])
def add_interview():
    if request.method == "POST":
        data = request.get_json()
        if 'round' not in data or 'scheduled_date' not in data or 'outcome' not in data:
            return {"error" : "Missing required fields"}, 400
        if not data['round'] or not data['scheduled_date'] or not data['outcome']:
            return {"error" : "Missing required fields"}, 400
        interview = Interviews(round=data['round'], scheduled_date=data['scheduled_date'], outcome=data['outcome'])
        db.session.add(interview)
        db.session.commit()
        return interview.to_dict(), 201

    if request.method == "GET":
        interviews = Interviews.query.all()
        interview_list = [interview.to_dict() for interview in interviews]
        return {
            "Interviews" : interview_list
            }, 200
    
@app.route('/interviews/<int:id>', methods=['PUT', 'GET', 'DELETE'])
def update_interview(id):
    if request.method == 'PUT':
        interview = Interviews.query.filter_by(id=id).first()
        if not interview:
            return {"error" : "Interview not found"}, 404
        data = request.get_json()
        if 'round' not in data or 'scheduled_date' not in data or 'outcome' not in data:
            return {"error" : "Missing required fields"}, 400
        if not data['round'] or not data['scheduled_date'] or not data['outcome']:
            return {"error" : "Missing required fields"}, 400
        interview.round = data['round']
        interview.scheduled_date = data['scheduled_date']
        interview.outcome = data['outcome']
        db.session.commit()
        return interview.to_dict()
    
    if request.method == 'GET':
        interview = Interviews.query.filter_by(id=id).first()
        if not interview:
            return {"error" : "Interview not found"}, 404
        return {
            "Interview" : interview.to_dict()
            }, 200
        
    if request.method == 'DELETE':
        interview = Interviews.query.filter_by(id=id).first()
        if not interview:
            return {"error" : "Interview not found"}, 404
        db.session.delete(interview)
        db.session.commit()
        return {"message" : "Interview deleted successfully"}, 200
    
@app.route('/jobapplications', methods=['POST', 'GET'])
def add_jobapplication():
    if request.method == 'POST':
        data = request.get_json()
        if "role" not in data or "status" not in data or "company_id" not in data or "interview_id" not in data:
            return {"error" : "Missing required fields"}, 400
        if not data['role'] or not data['status'] or not data['company_id'] or not data['interview_id']:
            return {"error" : "Missing required fields"}, 400
        jobapplication = JobApplications(role=data['role'], status=data['status'], notes=data['notes'], company_id=data['company_id'], interview_id=data['interview_id'])
        db.session.add(jobapplication)
        db.session.commit()
        return jobapplication.to_dict(), 201
    
    if request.method == 'GET':
        jobapplications = JobApplications.query.all()
        jobapplication_list = [jobapplication.to_dict() for jobapplication in jobapplications]
        return {"Job Application" : jobapplication_list}, 200

@app.route('/jobapplications/<int:id>', methods=['PUT', 'GET', 'DELETE'])
def update_jobapplication(id):
    if request.method == 'PUT':
        jobapplication = JobApplications.query.filter_by(id=id).first()
        if not jobapplication:
            return {"error" : "Job Application not found"}, 404
        data = request.get_json()
        if "role" not in data or "status" not in data or "company_id" not in data or "interview_id" not in data:
            return {"error" : "Missing required fields"}, 400
        if not data['role'] or not data['status'] or not data['company_id'] or not data['interview_id']:
            return {"error" : "Missing required fields"}, 400
        jobapplication.role = data['role']
        jobapplication.status = data['status']
        jobapplication.notes = data['notes']
        jobapplication.company_id = data['company_id']
        jobapplication.interview_id = data['interview_id']
        db.session.commit()
        return jobapplication.to_dict(), 200
    
    if request.method == 'GET':
        jobapplication = JobApplications.query.filter_by(id=id).first()
        if not jobapplication:
            return {"error" : "Job Application not found"}, 404
        return {
            "Job Application" : jobapplication.to_dict()
            }, 200
    
    if request.method == 'DELETE':
        jobapplication = JobApplications.query.filter_by(id=id).first()
        if not jobapplication:
            return {"error" : "Job Application not found"}, 404
        db.session.delete(jobapplication)
        db.session.commit()
        return {"message" : "Job Application deleted successfully"}

if __name__ == '__main__':
    app.run(debug=True)