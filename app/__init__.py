# Import flask and template operators
from flask import Flask, render_template,session,redirect,jsonify
from flask import *
from functools import wraps
# Import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object('config')

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)

# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

def requires_auth(f):
	@wraps(f)
	def decorated(*args, **kwargs):
		if 'user_id' not in session:
			return redirect('/')
		return f(*args, **kwargs)
	return decorated
 		 
# Import a module / component using its blueprint handler variable (mod_auth)
from app.students.controllers import mod_students
from app.courses.controllers import mod_courses
from app.course_faculty.controllers import mod_faculty
from app.Nominee.controllers import mod_nominees
from app.admin.controllers import mod_admin
##from app.enrolment.controllers import mod_enrolment

# Register blueprint(s)
app.register_blueprint(mod_students)
app.register_blueprint(mod_courses)
app.register_blueprint(mod_faculty)
app.register_blueprint(mod_nominees)
app.register_blueprint(mod_admin)
##app.register_blueprint(mod_enrolment)
# app.register_blueprint(xyz_module)
# ..

# Build the database:
# This will create the database file using SQLAlchemy
db.create_all()

@app.route('/')
def index():
    return render_template('login.html')
