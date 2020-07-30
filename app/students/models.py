from flask_sqlalchemy import SQLAlchemy
from app import db
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash

class Student(db.Model):
	__tablename__ = 'student'
	id=db.Column(db.Integer,primary_key=True,unique=True,autoincrement=True)
	roll=db.Column(db.Integer,unique=True)
	name=db.Column(db.String(20))
	email=db.Column(db.String(50),unique=True)
	password=db.Column(db.String(50))
	year=db.Column(db.String(20))
	CGPA=db.Column(db.Integer)
	Course_priority1=db.Column(db.String(20))
	Course_priority2=db.Column(db.String(20))
	Course_priority3=db.Column(db.String(20))
	status1=db.Column(db.String(120))
	status2=db.Column(db.String(120))
	status3=db.Column(db.String(120))
	
	def __init__(self,roll,name,email,password,year,CGPA,Course_priority1,Course_priority2,Course_priority3,status1,status2,status3):
		self.roll=roll
		self.name=name
		self.email=email
		self.password=generate_password_hash(password)
		self.year=year
		self.CGPA=CGPA
		self.Course_priority1=Course_priority1
		self.Course_priority2=Course_priority2
		self.Course_priority3=Course_priority3
		self.status1=status1
		self.status2=status2
		self.status3=status3
	def to_dict(self):
		return {'roll': self.roll, 'name':self.name, 'email': self.email, 'password':self.password, 'year':self.year, 'CGPA':self.CGPA, 'Course_priority1':self.Course_priority1, 'Course_priority2':self.Course_priority2, 'Course_priority3': self.Course_priority3,'status1':self.status1,'status2':self.status2,'status3':self.status3}
	def __repr__(self):
		return "User<%d>" % (self.roll)
	def check_password(self,password):
		return check_password_hash(self.password,password)
	
