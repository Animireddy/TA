from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for,jsonify
from app import db,requires_auth
import sqlalchemy
from app.students.models import Student
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
import re
mod_students = Blueprint('students', __name__)#url_prefix='/api'

@mod_students.route('/students', methods=['GET'])
@requires_auth
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
		"Course_priority3" : row.Course_priority3,
		"status1": row.status1,
		"status2": row.status2,
		"status3": row.status3
			}
		students.append(u);
	return jsonify(students=students)

@mod_students.route('/loginstudent1',methods=['GET'])
@requires_auth
def check_login():
	if 'user_id' in session:
		user = Student.query.filter(Student.id == session['user_id']).first()
		return jsonify(success = True,user = user)
	return jsonify(success = False),401

@mod_students.route('/loginstudent',methods=['POST'])
def loginstudent():
	try:
		val1 = request.form['email']
		val2 = request.form['password']
	except KeyError as e:
		return 'fail'
	user = Student.query.filter(Student.email == val1).first()
	if user is None:# or not user.check_password(val2):
		print('please register first or enter valid email')
		return 'fail'
	elif not user.check_password(val2):
		print('not correct password')
		return 'fail'
	else:
		session['user_id'] = user.id
		return jsonify(success=True,user=user.to_dict())

@mod_students.route('/logoutstudent',methods=['POST'])
@requires_auth
def logout():
	session.pop('user_id')
	return jsonify(success=True)

@mod_students.route('/addStudent',methods=['POST'])
def addStudent():
	arr = request.form['email']
	rol = request.form['roll']
	# truth = re.search("[0-9]{8}",rol)
	# if not truth or len(rol) != 8:
	# 	return 'fail_in_roll'
	# else:
	nam = request.form['name']
		# truth = re.search("^[A-Za-z\s]{1,}[\.]{0,1}[A-Za-z\s]{0,}$",nam)
		# if not truth:
		# 	return 'fail_in_name'
		# else:
		# 	text = arr
		# 	user = text[text.find("@")+1:].split()[0]
		# 	if user != "students.iiit.ac.in" and user != "faculty.iiit.ac.in":
		# 		return 'fail_in_email'
		# 	else:
	pas = request.form['password']
				# if len(pas) < 8:
				# 	return 'please keep length of password atleast 8'
				# else:
	yea = request.form['year']
					# truth = re.search("UG[0-6]{1}",yea)
					# if not truth:
					# 	return 'fail_in_year'
					# else:
	cgp = request.form['CGPA']
						# print(cgp)
						# if not cgp > '10' or cgp < '0':
						# 	return 'enter CGPA between 0 to 10'
						# else:
							
	Student1 = Student(rol,nam,arr,pas,yea,cgp,request.form['Course_priority1'],request.form['Course_priority2'],request.form['Course_priority3'],request.form['status1'],request.form['status2'],request.form['status3'])
	db.session.add(Student1)
	#	db.session.add(Student1)
	db.session.commit()
	return jsonify(success=True,message='success') # returnrender_template('student.html')


# BEFORE MODIFICATION#####################################################
	# arr = request.form['email']
	# rol = request.form['roll']
	# truth = re.search("[0-9]{8}",rol)
	# if not truth or len(rol) != 8:
	# 	return 'fail_in_roll'
	# else:
	# 	nam = request.form['name']
	# 	truth = re.search("^[A-Za-z\s]{1,}[\.]{0,1}[A-Za-z\s]{0,}$",nam)
	# 	if not truth:
	# 		return 'fail_in_name'
	# 	else:
	# 		text = arr
	# 		user = text[text.find("@")+1:].split()[0]
	# 		if user != "students.iiit.ac.in" and user != "faculty.iiit.ac.in":
	# 			return 'fail_in_email'
	# 		else:
	# 			pas = request.form['password']
	# 			if len(pas) < 8:
	# 				return 'please keep length of password atleast 8'
	# 			else:
	# 				yea = request.form['year']
	# 				truth = re.search("UG[0-6]{1}",yea)
	# 				if not truth:
	# 					return 'fail_in_year'
	# 				else:
	# 					cgp = request.form['CGPA']
	# 					print(cgp)
	# 					if not cgp > '10' or cgp < '0':
	# 						return 'enter CGPA between 0 to 10'
	# 					else:
							
	# 						Student1 = Student(rol,nam,arr,pas,yea,cgp,request.form['Course_priority1'],request.form['Course_priority2'],request.form['Course_priority3'],request.form['status1'],request.form['status2'],request.form['status3'])
	# 						db.session.add(Student1)
	# 						#	db.session.add(Student1)
	# 						db.session.commit()
	# 						return jsonify(success=True,message='success') # returnrender_template('student.html')
##			except IntegrityError as e:
##								return jsonify(success=False,message='user already registered')

@mod_students.route('/student_details', methods=['POST'])
@requires_auth
def Student_details():
	arr=[]
	course=request.form['course']
	user1=Student.query.filter(Student.Course_priority1 == course).all()
	user2=Student.query.filter(Student.Course_priority2 == course).all()
	user3=Student.query.filter(Student.Course_priority3 == course).all()
	for users in user1:
		if users.status1 != "dropped":
			u={
			"roll":users.roll,
			"CGPA":users.CGPA,
			"Course_priority":"priority1"
			}
			arr.append(u)
	for users in user2:
		if users.status2 != "dropped":
			u={
			"roll":users.roll,
			"CGPA":users.CGPA,
			"Course_priority":"priority2"
			}
			arr.append(u)
	for users in user3:
		if users.status3 != "dropped":
			u={
			"roll":users.roll,
			"CGPA":users.CGPA,
			"Course_priority":"priority3"
			}
			arr.append(u)
##	arr.append(users.roll)
##	for i in user1:
#		user=i.to_dict()
#		arr.append(user.roll)
#	for j in user2:
#		user=j.to_dict()
#		arr.append(user.roll)
#	for k in user3:
#		user=k.to_dict()
#		arr.append(user.roll)
	return jsonify(success=True,enrolled=arr)
@mod_students.route('/nominated', methods=['POST'])
@requires_auth
def nominated():
	arr=request.form.getlist('data[]',type=int)
	Course_name=request.form['Course_name']
	k='ass'
	print("array %s" % arr)
#	sd=len(arr)
#print("%s",(sd))
	for i in arr:
		admin=Student.query.filter(Student.roll == i).first()
		if admin.Course_priority1 == Course_name:
			admin.status1 = 'nominated'
			db.session.commit()
			k=admin.status1
		elif admin.Course_priority2 == Course_name:
			admin.status2 = 'nominated'
			db.session.commit()
			k=admin.status2		
		elif admin.Course_priority3 == Course_name:
			admin.status3 = 'nominated'
			db.session.commit()
			k=admin.status3
		else:
			continue
	return jsonify(success=True,status=k)
@mod_students.route('/lockstudent',methods=['POST'])
@requires_auth
def lock():
	Course_const=request.form['course']
	roll1=request.form['roll']
	admin1=Student.query.filter(Student.roll == roll1).first()
	sc1='a'
	if Course_const == 'ab1':
		admin1.status1 = 'locked'
		db.session.commit()
		admin1.status2 = 'already locked'
		db.session.commit()
		admin1.status3 = 'already locked'
		db.session.commit()
		sc1='status1'
	elif Course_const == 'ab2':
		admin1.status2 = 'locked'
		db.session.commit()
		admin1.status1 = 'already locked'
		db.session.commit()
		admin1.status3 = 'already locked'
		db.session.commit()
		sc1='status2'
	elif Course_const == 'ab3':
		admin1.status3 = 'locked'
		db.session.commit()
		admin1.status2 = 'already locked'
		db.session.commit()
		admin1.status1 = 'already locked'
		db.session.commit()
		sc1='status3'
	return jsonify(success=True,status=sc1)
@mod_students.route('/dropstudent',methods=['POST'])
@requires_auth
def drop():
	try:
		roll1=request.form['roll']
		admin1=Student.query.filter(Student.roll == roll1).first()
		admin1.status1 = 'dropped'
		db.session.commit()
		admin1.status2 = 'dropped'
		db.session.commit()
		admin1.status3 = 'dropped'
		db.session.commit()
		return jsonify(success=True)
	except:
		return 'fail'
