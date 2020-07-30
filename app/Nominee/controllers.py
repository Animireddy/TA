from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for,jsonify
from app import db
from app.students.models import Student
from app.courses.models import Course

mod_nominees = Blueprint('nominees',__name__)

@mod_nominees.route('/nominees',methods = ['GET'])
def default_all_students():
	students=[];
	list = Student.query.all()
	for row in list:
##                      c = Enroll.query.filter(row.roll == Enroll.roll).all()
##                      a = [];
##                      for i in c:
##                              a.append(i.code)

		u={
			"roll" : row.roll,
            "name" : row.name,
            "email": row.email,
            "password": row.password,
            "year" : row.year,
            "CGPA" : row.CGPA,
            "Course_priority1" : row.Course_priority1,
            "Course_priority2" : row.Course_priority2,
            "Course_priority3" : row.Course_priority3,
			"status_1"    :'not accepted',
			"status_2"    :'not accepted',
			"status_3"    :'not accepted'
             	}
		students.append(u);
		return jsonify(nominees=students)
