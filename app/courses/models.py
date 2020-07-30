from flask_sqlalchemy import SQLAlchemy
from app import db

class Course(db.Model):
	__tablename__= 'course'
	Course_id=db.Column(db.String(20),primary_key=True,unique=True)
	Course_name=db.Column(db.String(20))
	def __init__(self,Course_id, Course_name):
		self.Course_id=Course_id
		self.Course_name=Course_name

