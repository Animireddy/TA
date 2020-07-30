from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for,jsonify
from app import db,requires_auth
from app.students.models import Student
from app.courses.models import Course
from app.admin.models import Admin
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
import re

###from app.enrolment.models import Enroll
mod_admin = Blueprint('admin', __name__)

@mod_admin.route('/admin', methods=['GET'])
##@requires_auth
def get_Admin():
	facts=[];
	list = Admin.query.all()
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
			}
		facts.append(u);
	return jsonify(admin=facts)
#@mod_admin.route('/loginadmin1',methods=['GET'])
#def check_login():
#	if 'user_id' in session:
#		user = Student.query.filter(Student.id == session['user_id']).first()
#		return jsonify(success = True,user = user)
#	return jsonify(success = False),401

@mod_admin.route('/logoutadmin',methods=['POST','GET'])
def logout():
	session.pop('user_id')
	return jsonify(success = True) 	

@mod_admin.route('/addAdmin',methods=['POST'])
def addAdmin():
	nam = request.form['name']
	ema = request.form['email']
	pas = request.form['password']
	# truth = re.search("^[A-Za-z\s]{1,}[\.]{0,1}[A-Za-z\s]{0,}$",nam)
	# if not truth:
	# 	return 'fail_in_name'
	# else:
	# 	text = ema
	# 	user = text[text.find("@")+1:].split()[0]
	# 	if user != "iiit.ac.in":
	# 		return 'fail_in_email'
	# 	else:
	# 		if len(pas) < 8:
	# 			return 'please keep length of password atleast 8'
	# 		else:
	try:
#						addCourse()
		Cour = Admin(nam,ema,pas)
		db.session.add(Cour)
		db.session.commit()
		return jsonify(success=True,message='success')
	except:
		return jsonify(success=False,message='already registered')
#@mod_faculty.route('/courselist', methods=['POST'])
#def get_all_Courses():
#	facts=[];
#	list = Course_Faculty.query.all()
#	for row in list:
#	u={
#		"Course_id" : row.Course_id,
#		"Course_name" : row.Course_name
#		}
#		facts.append(row.Course_name);
#	print facts;
#	return jsonify(success=True, courselist1 = facts)
@mod_admin.route('/loginadmin', methods=['POST'])
def Displaydata():
	try:
		val1=request.form['email']
		val2=request.form['password']
	except KeyError as e:
		return 'fail'
	user=Admin.query.filter(Admin.email == val1).first()
	if user is None or not user.check_password(val2):
		return 'fail'
	else:
		session['user_id']=user.id
		list = Course.query.all()
		arr=[]
		for row in list:
			list1=Student.query.filter(Student.Course_priority1 == row.Course_name).all()
			list2=Student.query.filter(Student.Course_priority2 == row.Course_name).all()
			list3=Student.query.filter(Student.Course_priority3 == row.Course_name).all()
			students=[]
			for row1 in list1:
				if row1.status1 is  "nominated" or "locked":
					print("aasaaaa")
					students.append(row1.roll)
			for row1 in list2:
				if row1.status2 is "nominated" or "locked":
					students.append(row1.roll)
					print("aasaaaa")
			for row1 in list3:
				if row1.status3 is "nominated" or "locked":
					students.append(row1.roll)
					print(arr)
			u={
			"Course_id":row.Course_id,
			"Course_name":row.Course_name,
			"students":students
			}
			arr.append(u)
		print(arr)
		return jsonify(success=True,data=arr)
@mod_admin.route('/tas_list', methods=['POST'])
def selected():
	try:
		arr=request.form.getlist('data[]',type=int)
		Course_name=request.form['Course_name']
		k='ass'
		print("array %s" % arr)
#   sd=len(arr)
#print("%s",(sd))
		for i in arr:
			admin=Student.query.filter(Student.roll == i).first()
			if admin.Course_priority1 == Course_name:
				admin.status1 = 'selected'
				db.session.commit()
				k=admin.status1
			elif admin.Course_priority2 == Course_name:
				admin.status2 = 'selected'
				db.session.commit()
				k=admin.status2
			elif admin.Course_priority3 == Course_name:
				admin.status3 = 'selected'
				db.session.commit()
				k=admin.status3
			else:
				continue
		return jsonify(success=True,status=k)
	except:
		return 'fail'

	
