from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for,jsonify
from app import db,requires_auth
from app.courses.models import Course
from app.course_faculty.models import Course_Faculty
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
import re

###from app.enrolment.models import Enroll
mod_faculty = Blueprint('course_faculty', __name__)

@mod_faculty.route('/course_faculty', methods=['GET'])
@requires_auth
def get_all_faculty():
	facts=[];
	list = Course_Faculty.query.all()
	for row in list:
##		print(row.Faculty_id)
##			c = Enroll.query.filter(row.roll == Enroll.roll).all()
##			a = [];
##			for i in c:
##				a.append(i.code)

		u={
		"name" : row.name,
		"email": row.email,
		"password": row.password,
		"Faculty_id": row.Faculty_id,
		"Course_id" : row.Course_id,
		"Course_name" : row.Course_name,
		"Course_description" : row.Course_description
			}
		facts.append(u);
	return jsonify(course_faculty=facts)
@mod_faculty.route('/loginfaculty1',methods=['GET'])
def check_login():
	if 'user_id' in session:
		user = Course_Faculty.filter(Course_Faculty.id == session['user_id']).first()
		return jsonify(success=False),401

@mod_faculty.route('/loginfaculty',methods=['POST'])
def loginfaculty():
	try:
		val1 = request.form['email']
		val2 = request.form['password']
	except KeyError as e:
		return 'fail'
	user = Course_Faculty.query.filter(Course_Faculty.email == val1).first()
	if user is None or not user.check_password(val2):
		print('No email')
		return 'fail'
#if not user.check_password(val2):
#		print('password wrong')
#		return 'fail'
	else:
		session['user_id'] = user.id
		return jsonify(success=True,user=user.to_dict())	

@mod_faculty.route('/logoutfaculty',methods=['POST'])
def logout():
	session.pop('user_id')
	return jsonify(success = True) 	

@mod_faculty.route('/addFaculty',methods=['POST'])
def addFaculty():
	nam = request.form['name']
	ema = request.form['email']
	pas = request.form['password']
	fid = request.form['Faculty_id']
	cid = request.form['Course_id']
	cna = request.form['Course_name']
	# truth = re.search("^[A-Za-z\s]{1,}[\.]{0,1}[A-Za-z\s]{0,}$",nam)
	# if not truth:
	# 	return 'fail_in_name'
	# else:
	# 	text = ema
	# 	user = text[text.find("@")+1:].split()[0]
	# 	if user != "faculty.iiit.ac.in":
	# 		return 'fail_in_email'
	# 	else:
	# 		if len(pas) < 8:
	# 			return 'please keep length of password atleast 8'
	# 		else:
	# 			truth = re.search("20160[0-9]{3}",fid)
	# 			if not truth:
	# 				return 'fail_in_id'
	# 			else:
	# 				truth = re.search("[A-Z]{3}[0-9]{3}",cid)	
	# 				if not truth:
	# 					return 'fail_in_course_id'
	# 				else:
	# 					truth = re.search("[a-zA-z]",cna)
	# 					if not truth:
	# 						return 'fail_in_course_name'
	# 					else:
	try:
		Cour = Course_Faculty(nam,ema,pas,fid,cid,cna,request.form['Course_description'])
		db.session.add(Cour)
		db.session.commit()
		return jsonify(success=True,message='success')
	except:
		return jsonify(success=False,message='already registered')
@mod_faculty.route('/courselist', methods=['POST'])
def get_all_Courses():
	facts=[];
	list = Course_Faculty.query.all()
	for row in list:
#	u={
#		"Course_id" : row.Course_id,
#		"Course_name" : row.Course_name
#		}
		facts.append(row.Course_name);
	print(facts);
	return jsonify(success=True, courselist1 = facts)

