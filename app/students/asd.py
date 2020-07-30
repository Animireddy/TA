from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for,jsonify
from app import db
from app.students.models import Student
import re
mod_students = Blueprint('students', __name__)

@mod_students.route('/students', methods=['GET'])
def get_all_students():
	students=[];
	list = Student.query.all()
	for row in list:
##			c = Enroll.query.filter(row.roll == Enroll.roll).all()
##			a = [];
##			for i in c:
##				a.append(i.code)

		u={
		"roll" : row.roll,
		"name" : row.name,
		"email": row.email,
		"password": row.password,
		"year" : row.year,
		"CGPA" : row.CGPA,
		"Course_priority1" : row.Course_priority1,
		"Course_priority2" : row.Course_priority2,
		"Course_priority3" : row.Course_priority3
			}
		students.append(u);
	return jsonify(students=students)
@mod_students.route('/loginstudent',methods=['GET'])
def loginstudent():
	val1=request.args.get('email')
	val2=request.args.get('password')
	val3=Student.query.add_columns(Student.roll,Student.name,Student.email,Student.password,Student.Course_priority1,Student.Course_priority2,Student.Course_priority3).filter(Student.email.like(val1)).all()
	print(val3)
	if(val3[0].password == val2):
		return jsonify(students=val3)
@mod_students.route('/addStudent',methods=['POST'])
def addStudent():
	arr = request.form['email']
	rol = request.form['roll']
	truth = re.search("[0-9]{8}",rol)
	if not truth:
		return 'fail_in_roll'
	else:
		nam = request.form['name']
		truth = re.search("^[A-Za-z\s]{1,}[\.]{0,1}[A-Za-z\s]{0,}$",nam)
		if not truth:
			return 'fail_in_name'
		else:
			text = arr
			user = text[text.find("@")+1:].split()[0]
			if user != "students.iiit.ac.in" and user != "faculty.iiit.ac.in":
				return 'fail_in_email'
			else:
				pas = request.form['password']
				if len(pas) < 8:
					return 'please keep length of password atleast 8'
				else:
					yea = request.form['year']
					truth = re.search("UG[0-6]{1}",yea)
					if not truth:
						return 'fail_in_year'
					else:
						cgp = request.form['CGPA']
						if not cgp > 10 or cgp < 0:
							return 'enter CGPA between 0 to 10'
						else:
							try:
								Student1 = Student(rol,nam,arr,pas,yea,cgp,request.form['Course_priority1'],request.form['Course_priority2'],request.form['Course_priority3'])
								db.session.add(Student1)
								db.session.add(Student1)
								db.session.commit()
								return 'success' # return render_template('student.html')
							except:
								return 'user already registered'
