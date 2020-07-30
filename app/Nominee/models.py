from flask_sqlalchemy import SQLAlchemy
from app import db

class Nominee(db.Model):
	__tablename__ = 'nominee'
	id = db.Column(db.Integer,primary_key = True,unique = true,autoincrement = True)
	roll = db.Column(db.Integer,db.Foreignkey(student.roll))
	course_id = db.Column(db.Integer,db.Foreignkey(Course_id))
	
	def __init__(self,roll,course_id):
		self.roll = roll	
		self.course_id = course_id
 
