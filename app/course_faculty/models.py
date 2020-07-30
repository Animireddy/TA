from flask_sqlalchemy import SQLAlchemy
from app import db
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash

class Course_Faculty(db.Model):
	__tablename__ = 'faculty'
	id=db.Column(db.Integer,primary_key=True,unique=True,autoincrement=True)
	name=db.Column(db.String(120))
	email=db.Column(db.String(150),unique=True)
	password=db.Column(db.String(150))
	Faculty_id=db.Column(db.Integer,unique=True)
	Course_id=db.Column(db.String(120),unique=True)
	Course_name=db.Column(db.String(120),unique=True)
	Course_description=db.Column(db.String(120))
	def __init__(self,name,email,password,Faculty_id,Course_id,Course_name,Course_description):
		self.name=name
		self.email=email
		self.password=generate_password_hash(password)
		self.Faculty_id=Faculty_id
		self.Course_id=Course_id
		self.Course_name=Course_name
		self.Course_description=Course_description
	def to_dict(self):
		return {'name':self.name, 'email': self.email, 'password':self.password, 'Faculty_id':self.Faculty_id, 'Course_id':self.Course_id, 'Course_name':self.Course_name,'Course_description':self.Course_description}
	def __repr__(self):
		return "User<%d>" % (self.Faculty_id)
	def check_password(self,password):
		return check_password_hash(self.password,password)
