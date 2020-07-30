from flask import Blueprint, request, render_template, \
	                  flash, g, session, redirect, url_for,jsonify
from app import db
from app.courses.models import Course
from app.course_faculty.models import Course_Faculty
##from app.enrolment.models import Enroll
mod_courses = Blueprint('courses', __name__)

@mod_courses.route('/courses', methods=['GET'])
def get_all_courses():
	courses = [];
	list = Course.query.all()
	for row in list:
##	c=Enroll.query.filter(row.code == Enroll.code).all()
##		a=[];
##		for i in c:
##			a.append(i.roll)
		u = {
	    "Course_id" : row.Course_id,
	    "Course_name" : row.Course_name,
	   	 ##"students" : a
	    }
		courses.append(u);
	return jsonify(courses=courses)
@mod_courses.route('/addCourse', methods=['POST'])
def add_course():
	try:
		course_id=request.form['Course_id']
		course_name=request.form['Course_name']
		Cour1=Course(course_id,course_name)
		db.session.add(Cour1)
		db.session.commit()
		return jsonify(success=True)
	except:
		return jsonify(success=False)
	
#@mod_courses.route('/addCourse',methods=['POST'])
#def addCourse():	
#	Course1=Course(request.form['Course_id'],request.form['Course_name'])
#	list = Course_faculty.query.all()
#	for row in list:
#	Course_id = request.form['Course_id']
#	Course_name = request.form['Course_name']
#	try:
#		Course_id=row.Course_id
#		Course_name=row.Course_name
#		course1 = Course(Course_id,Course_name)
#		db.session.add(course1)
#		db.session.commit()
#	return jsonify(status = "true")
#	except:
#		return jsonify(status="false")
#courses = [];
#	list = Course.query.all()
#	for row in list:
#		u = {
#		"Course_id" : row.Course_id,
#	    "Course_name" : row.Course_name,
#	    }
#		courses.append(u);
#	return jsonify(courses=courses)
#@mod_courses.route('/courselist',methods=['POST'])
#def courselist():
#	arr=[]
#	list = Course.query.all()
#	arr=list
#	return jsonify(courselist=arr,success=True)


