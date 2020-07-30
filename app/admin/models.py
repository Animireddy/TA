from flask_sqlalchemy import SQLAlchemy
from app import db
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash

class Admin(db.Model):
	__tablename__ = 'admin'
	id=db.Column(db.Integer,primary_key=True,unique=True,autoincrement=True)
	name=db.Column(db.String(120))
	email=db.Column(db.String(150),unique=True)
	password=db.Column(db.String(150))
	def __init__(self,name,email,password):
		self.name=name
		self.email=email
		self.password=generate_password_hash(password)
	def to_dict(self):
		return {'name':self.name, 'email': self.email, 'password':self.password}
	def __repr__(self):
		return "User<%r>" % (self.name)
	def check_password(self,password):
		return check_password_hash(self.password,password)
