function hide_all_containers(){
	console.log("hide_all_containers");
	$('#loginform').addClass("hidden");
	$('#register_student').addClass("hidden");
	$('#register_faculty').addClass("hidden");
	$('#student_profile').addClass("hidden");
	$('#faculty_profile').addClass("hidden");
	$('#register_admin').addClass("hidden");
	$('#admin_profile').addClass("hidden");
};
var email_t;
var pass_t;
var fun1=function(){
	email_t=document.getElementById("email1").value;
	pass_t=document.getElementById("pass1").value;
	var str = email_t.substring(email_t.indexOf("@") + 1);
	console.log(str);
	console.log(email_t);
	console.log(pass_t);

	if(str=='faculty.iiit.ac.in')
	{
		window.location.hash='FacultyProfile';
	}
	else if(str=='students.iiit.ac.in' | str=='research.iiit.ac.in')
	{
		window.location.hash='StudentProfile';
	}
	else if(str=='iiit.ac.in')
	{
		window.location.hash='AdminProfile';
	}
	else
	{
		document.getElementById("email1").value="";
		document.getElementById("pass1").value="";
		alert('please enter either faculty or student information *');
		window.location.hash="index";
	}
}
var fun2a=function(){
	window.location.hash='register_Student';
}
var fun2b=function(){
	window.location.hash='register_Faculty';
}
var fun2c=function(){
	window.location.hash='register_Admin'
}
var fun3=function(){
	window.location.hash='StudentProfile';
}
var fun4=function(){
	window.location.hash='FacultyProfile';
}
function get_window_hash_path() {
  return location.hash.substring(1);
};
function navigate(path){
	var current=window.location.href;
	window.location.href = current.replace(/#(.*)$/,'')+'#' + path;
};
function register_onhashchange_handlers(handler_functions){
	$(window).on("hashchange",function(e){
		hash_path = get_window_hash_path();
		console.log("new hash: ",hash_path);
		if(handler_functions.hasOwnProperty(hash_path)){
		handler_functions[hash_path]();	
		}
		else{
			console.warn('no handler for ${hash_path}');
		}
	});
};
window.onload = function(){
	register_onhashchange_handlers({
		index:login_handler,
		register_Student:register_Student_handler,
		register_Faculty:register_Faculty_handler,
		register_Admin:register_Admin_handler,
		StudentProfile:student_profile_handler,
		FacultyProfile:faculty_profile_handler,
		AdminProfile:admin_profile_handler,
	})
	let current_hash = get_window_hash_path();
	console.log(current_hash);
    if(current_hash===""){
		console.log(current_hash);
	    current_hash="index";
	    navigate(current_hash);
    }
}
function login_handler(){
	hide_all_containers();
	$("#loginform").removeClass("hidden");
	$("#loginform #button1")[0].addEventListener("click",fun1)
	$("#loginform #button2a")[0].addEventListener("click",fun2a)
	$("#loginform #button2b")[0].addEventListener("click",fun2b)
	$("#loginform #button2c")[0].addEventListener("click",fun2c)	
}
var animi='not okk';
function register_Student_handler(){
	hide_all_containers();
	courses();
	$('#register_student').removeClass("hidden")
	console.log('awfbbesg');
	//courses();
	$('#button3')[0].addEventListener("click",back1)
}
function register_Faculty_handler(){
	hide_all_containers();
	console.log("ASAs");
	$('#register_faculty').removeClass("hidden")
	//$('#button4')[0].on("click",back2)ff
	$('#button4')[0].addEventListener("click",back2)
}
function register_Admin_handler(){
	hide_all_containers();
	console.log("Aaqwe");
	$('#register_admin').removeClass("hidden")
	//$('#button4')[0].on("click",back2)ff
	$('#button_admin')[0].addEventListener("click",back4)
}

var kfc;
function student_profile_handler(){
	console.log(email_t);
	displayStudent();
	if(kfc!=='fail')
	{
		hide_all_containers();
		$("#student_profile").removeClass("hidden");
	}
};
var lays;
function faculty_profile_handler(){
	console.log(email_t);
	displayFaculty();
	if(lays!=='fail')
	{
		hide_all_containers();
		$("#faculty_profile").removeClass("hidden");
	}

};
var kids1;
function admin_profile_handler(){
	console.log(email_t);
	displayAdmin();
	if(kids1!=='fail')
	{
		hide_all_containers();
		$("#admin_profile").removeClass("hidden");
	}

};
var displayStudent=function(){
	$.post('http://127.0.0.1:5050/loginstudent',{email: email_t,password: pass_t},function(response){
		console.log(response);
		kfc=response;
		if(response =='fail')
		{
			alert('Invalid Credentials');
			console.log(response);
			window.location.hash='index'
			document.getElementById("email1").value=""
			document.getElementById("pass1").value=""
		}
		else
		{
			arr=response.user;
			console.log(1);
			console.log(response);
			console.log(arr);
			document.getElementById("names").innerHTML=arr.name
			document.getElementById("rolls").innerHTML=arr.roll
			document.getElementById("years").innerHTML=arr.year
			document.getElementById("priorty1s").innerHTML=arr.Course_priority1
			document.getElementById("priorty2s").innerHTML=arr.Course_priority2
			document.getElementById("priorty3s").innerHTML=arr.Course_priority3
			document.getElementById("status1s").innerHTML=arr.status1
			document.getElementById("status2s").innerHTML=arr.status2
			document.getElementById("status3s").innerHTML=arr.status3

			if(arr.status1 =='nominated')
			{
				console.log('vbgebjvgew');
				document.getElementById("btn2").disabled = false;
			}
			if(arr.status2 =='nominated')
			{
				console.log('vbgebjvgew');
				document.getElementById("btn22").disabled = false;
			}			
			if(arr.status3=='nominated')
			{
				console.log('vbgebjvgew');
				document.getElementById("btn222").disabled = false
			}

			buttonclick(arr);
		}
		}).fail(function(){
		window.location.hash="index";
		alert('Error!!!');
		console.log('error');
	})
}
var displayAdmin=function(){
	console.log(email_t);
	console.log(pass_t);
	$.post('http://127.0.0.1:5050/loginadmin',{email: email_t,password: pass_t},function(response){
		console.log(response);
		kids1=response;
		if(response =='fail')
		{
			alert('Invalid Credentials');
			console.log(response);
			document.getElementById("email1").value=""
			document.getElementById("pass1").value=""
		}
		else
		{
			arr=response.data;
			console.log(1);
			console.log(response);
			console.log(arr);
			var i;
			for(i=0;i<arr.length;i++)
			{
				students11(arr[i].students,arr[i].Course_name);
			}
			disc=arr;
			$("#button_ta").on('click',function(){get_tas(disc)});
		}
		}).fail(function(){
		alert('Error!!!');
		window.location.hash='index';
		console.log('error');
	})
}
function buttonclick(arr)
{
	var roll1=arr.roll
	var sc1='ab0';
	if(arr.status1=='nominated'){
		$("#btn2").on('click',function(){
			console.log('asdfghqw')
			document.getElementById("btn222").disabled = true;
			document.getElementById("btn22").disabled = true;
			sc1='ab1';
			document.getElementById("status1s").innerHTML="locked"
			document.getElementById("status2s").innerHTML="already locked"
			document.getElementById("status3s").innerHTML="already locked"

			console.log(sc1);
			$.post('http://127.0.0.1:5050/lockstudent',{roll:roll1, course:sc1}, function(response){
				//change at backend (remove remaining courses field of various priority and keep "")
			console.log(response);
			alert('priority1 is locked');
		})
	})
	}
	else if(arr.status2=='nominated'){
		$("#btn22").on('click',function(){
			console.log('1aaa');
			document.getElementById("btn222").disabled = true;
			document.getElementById("btn2").disabled = true;
			sc1='ab2';
			document.getElementById("status2s").innerHTML="locked"
			document.getElementById("status1s").innerHTML="already locked"
			document.getElementById("status3s").innerHTML="already locked"

			$.post('http://127.0.0.1:5050/lockstudent',{roll:roll1, course:sc1}, function(response){
				//change at backend (remove remaining courses field of various priority and keep "")
			console.log(response);
			alert('priority2 is locked');
		})
	})
	}
	else if(arr.status3=='nominated'){
		$("#btn222").on('click',function(){
			document.getElementById("btn2").disabled = true;
			document.getElementById("btn22").disabled = true;
			sc1='ab3';
			document.getElementById("status3s").innerHTML="locked"
			document.getElementById("status2s").innerHTML="already locked"
			document.getElementById("status1s").innerHTML="already locked"
			$.post('http://127.0.0.1:5050/lockstudent',{roll:roll1, course:sc1}, function(response){
				//change at backend (remove remaining courses field of various priority and keep "")
			console.log(response);
			alert('priority3 is locked');
		})
	})
	}
	else if($("#drop").on('click',function(){
		document.getElementById("btn2").disabled = true;
		document.getElementById("btn22").disabled = true;
		document.getElementById("btn222").disabled = true;
		document.getElementById("status1s").innerHTML="dropped"
		document.getElementById("status2s").innerHTML="dropped"
		document.getElementById("status3s").innerHTML="dropped"
		$.post('http://127.0.0.1:5050/dropstudent',{roll:roll1},function(response){
			console.log(response);
			document.getElementById("dropN").innerHTML="Student dropped from nomination"
			alert('student dropeed from nomination');
		})	
	}));
}

var var1;
var displayFaculty=function(){
$.post('http://127.0.0.1:5050/loginfaculty',{email: email_t,password: pass_t},function(response){
		console.log(response);
		lays=response;
		if(response =='fail')
		{
			alert('Invalid Credentials');
			console.log(response);
			window.location.hash='index'
			document.getElementById("email1").value=""
			document.getElementById("pass1").value=""
		}
		else
		{
			var arr12=response.user;
			console.log(1);
			console.log(response);
			console.log(arr12);
			document.getElementById("name4").innerHTML=arr12.name
			document.getElementById("fac_id4").innerHTML=arr12.Faculty_id
			document.getElementById("cou_id4").innerHTML=arr12.Course_id
			document.getElementById("cou_name4").innerHTML=arr12.Course_name
			document.getElementById("cou_des4").innerHTML=arr12.Course_description
			console.log(arr12.Course_name);
			student_details(arr12.Course_name);
			var1=arr12.Course_name;
		}
		}).fail(function(){
		window.location.hash="index";
		alert('Error!!!');
		console.log('error');
	})
}
var array;
var arr4=[];
function student_details(course){
	$.post('http://127.0.0.1:5050/student_details',{course:course},function(response){
		console.log(response);
		array=response.enrolled;
		students(array,course);
	})
}
function func4(){
	var ret=false;
	$.post('http://127.0.0.1:5050/courselist',{},function(response){
		console.log(response);
		arr4=response.courselist1;	
	}).fail(function(){
		console.log('Error!!!');
		alert('Error!!!');
	});
	return ret;
}
var courses=function() {
	var arr=func4();
	var n=arr4.length;
	console.log(n);
	var i;
	var str="<option>"+"select a course"+"</option>"
	for(i=0;i<n;i++)
	{
		str=str+"<option value=" + arr4[i] + ">" + arr4[i]+ "</option>"
	}
	document.getElementById("lcourses1").innerHTML=str
	document.getElementById("lcourses2").innerHTML=str
	document.getElementById("lcourses3").innerHTML=str
	
};
var students=function(arr,course){
	console.log(arr);
	if(arr.length!=0)
	{
			document.getElementById("button6").disabled=false;
	}
	var str1='<input type=' + '"checkbox"' + ' '+'name=' + '"students_selected"' + 'class='+ '"messageCheckbox"';
	var str3=str1;
	var i;
//	for(i=0;i<arr.length-1;i++)
//	{
	//	str1=str1 + 'value=' +arr[i] + '>' +arr[i]+'<br/>'+str3;
	    		
//		console.log(str1);
//	} 
//	str1=str1 + 'value=' + arr[arr.length-1] +'>' +arr[arr.length-1]+'<br/>';
	var strr='';
	for(i=0;i<arr.length;i++)
	{
		strr+='<tr>'+'<td>'+arr[i].roll+'</td>'+'<td>'+arr[i].CGPA+'</td>'+'<td>'+arr[i].Course_priority+'</td>' +'<td>'+'<input type='+'"checkbox"'+''+'name='+'"students_selected"'+'class='+'"messageCheckbox"';
		strr+=''+'value='+arr[i].roll+'>'+arr[i].roll+'</td>'+'</tr>'; 
	}
	//document.getElementById("dataS").innerHTML=str1;
	document.getElementById("dataS").innerHTML=strr;
	//document.getElementById("dataSC").innerHTML=document.getElementById("dataSC").innerHTML+str2
	$("#button6").on("click",func1);
}
var students11=function(arr,course){
	console.log(arr);
	console.log(course);
	var str1='<input type=' + '"checkbox"' + ' '+'name=' + course + ' ' + 'class='+ '"messageCheckbox"';
	var str3=str1;
	var i;
	for(i=0;i<arr.length-1;i++)
	{
		str1=str1 +' '+ 'id=' + course + ' '+ 'value=' +arr[i] + '/>' +arr[i]+'<br/>'+str3;
	} 
	str1=str1 + ' '+ 'id=' + course + ' '+'value=' + arr[arr.length-1] +'/>' +arr[arr.length-1]+'<br/>';
	var str2='<label>' + course + '</label>' + ':' +'<br/>'+ str1 +'<br/>';
	console.log(str2);
	//document.getElementById("dataS").innerHTML=str1;
	document.getElementById("dataSC").innerHTML=document.getElementById("dataSC").innerHTML+str2
	//$("#button6").on("click",func1);
}

$.ajaxSetup({async: false});
var back1=function(){
	var ret=false;
	console.log("1234");
	$.post('http://127.0.0.1:5050/addStudent',{roll:$("#roll2").val(),
			name:$("#name2").val(),
			email:$("#email2").val(),
			password:$("#pass2").val(),
			year:$("#year2").val(),
			CGPA:$("#cgpa2").val(),
			Course_priority1:$("#lcourses1").find(":selected").text(),
			Course_priority2:$("#lcourses2").find(":selected").text(),
			Course_priority3:$("#lcourses3").find(":selected").text(),
			status1:'not yet nominated',
			status2:'not yet nominated',
			status3:'not yet nominated'},function(data){
				console.log(data.success)
				if(data.success==true)
				{
					console.log(1);
					email_t=$("#email2").val(),
					pass_t=$("#pass2").val(),
					student_profile_handler();
					//alert('succesfully registered');
				}
				else{
				//alert(response);
				console.log(data);
			}
			}).fail(function(){
				alert('Error!!!');
			});
			return ret;
};
function get_check_box(response) {
	console.log(response);
	var checkboxes = document.getElementsByName(response);
	console.log(checkboxes);
	console.log(checkboxes[0].value);
	var checkboxesChecked = [];
	for(var i=0;i<checkboxes.length;i++) {
		//if(document.getElementById(course).val()==course || response=='students_selected')
		//{
		if(checkboxes[i].checked) {
			checkboxesChecked.push(parseInt(checkboxes[i].value));
		}
		}
	//}
	return checkboxesChecked;
}
function get_check_box1(course) {
	console.log(course);
	var checkboxes = document.getElementsByName(course);
	//var train = document.getElementsById(course);
	//console.log(train);
	console.log(checkboxes);
	var checkboxesChecked = [];
	//var j=0;
	for(var i=0;i<checkboxes.length;i++) {
		//if(train[i] == course)
		//{
		if(checkboxes[i].checked) {
			checkboxesChecked.push(parseInt(checkboxes[i].value));
		//}
		}
	}
	//}
	return checkboxesChecked;
}
var var2;
function func1(){
	var2=get_check_box('students_selected');
	console.log(var2);
	$.post('http://127.0.0.1:5050/nominated',{Course_name:var1, data:var2},function(response){
		//alert('selected students are successfully nominated');
		console.log(response);
	}).fail(function(){
		alert('Error!!!');
	})
}
/*$.ajaxSetup({async: false}),
function back4(){	
	var ret = false;
	console.log(12345);
	$.post('http://127.0.0.1:5050/addCourse',{Course_id:$('#cou_id3').val(),
		Course_name:$("cou_name3").val()},function(data){
			alert(data);
			console.log(data);
			console.log('courses added');
			}).fail(function(){
			alert('Error!!!!')
		});
		return ret;
}*/


$.ajaxSetup({async: false});
var back2=function(){
	var ret=false;
	console.log(123456);
	$.post('http://127.0.0.1:5050/addFaculty',{name:$("#name3").val(),
			email:$("#email3").val(),
			password:$("#pass3").val(),
			Faculty_id:$("#fac_id3").val(),
			Course_id:$("#cou_id3").val(),
			Course_name:$("#cou_name3").val(),
			Course_description:$("#cou_des3").val()},function(response){
					console.log(response);
					if(response.success==true)
					{	
						console.log(1);
						email_t=$("#email3").val(),
						pass_t=$("#pass3").val(),
						courseadd();
						window.location.hash='FacultyProfile';
						//alert('successfully registered')
					}
					else
					{
						alert('response')
					}
				}).fail(function(){
				alert('Error!!!');
			});			
			return ret;
}
$.ajaxSetup({async: false});
var courseadd=function(){
	console.log(2);
	cou_id3=$("#cou_id3").val();
	cou_name3=$("#cou_name3").val();
	console.log(cou_name3);
	console.log(cou_id3);
	$.post('http://127.0.0.1:5050/addCourse',{Course_id:$("#cou_id3").val(),
		Course_name:$("#cou_name3").val()},function(response){
				console.log(response);
		}).fail(function(){
			alert('Error!!!');
		})
};

$.ajaxSetup({async: false});
var back4=function(){
	var ret=false;
	console.log(123456);
	$.post('http://127.0.0.1:5050/addAdmin',{name:$("#name_admin").val(),
			email:$("#email_admin").val(),
			password:$("#pass_admin").val()
			},function(response){
					console.log(response);
					//alert(response);
					if(response.success==true)
					{	
						console.log(1);
						email_t=$("#email_admin").val(),
						pass_t=$("#pass_admin").val(),
						window.location.hash = 'AdminProfile';
					}
				}).fail(function(){
				alert('Error!!!');
			});			
			return ret;
}
$.ajaxSetup({async: false});	
var logoutStudent11=function(){
	console.log('asdasd');
	$.post('http://127.0.0.1:5050/logoutstudent',{roll:$("#roll2").val()},function(response){
	//	alert(response);
		console.log(response);
		window.location.hash='index'
		document.getElementById("email1").value=""
		document.getElementById("pass1").value=""
	}).fail(function(){
		alert("NOT LOGGED OUT:)");
	});
}

$.ajaxSetup({async: false});	
var logoutFaculty11=function(){
	console.log('asdasd');
	$.post('http://127.0.0.1:5050/logoutfaculty',{roll:$("#fac_id4").val()},function(response){
	//	alert(response);
		console.log(response);
		window.location.hash='index'
		document.getElementById("email1").value=""
		document.getElementById("pass1").value=""
	}).fail(function(){
		alert("NOT LOGGED OUT:)");
	});
}
function get_tas(disc){
	console.log(disc);
	var arrf=[];
	var array=[];
	var Cour_name;
	var j;
	var flag=0;
	for(i=0;i<disc.length;i++)
	{
		Cour_name=disc[i].Course_name;
		var studs=disc[i].students;
		console.log(Cour_name);
		var res=get_check_box(Cour_name);
		console.log(res);
		for(j=0;j<res.length;j++)
		{	
			console.log('1a');
			console.log(arrf.includes(res[j]));
			if(arrf.includes(res[j])==true)
			{
				console.log('2a');
				flag=1;
				break;
			}
			array.push(res);

		}
		arrf.push.apply(arrf,res);
	}
	console.log(flag);
	if(flag==0)
	{
		//alert('successfully selected');
	for(i=0;i<array.length;i++)
	{
		console.log(array[i]);
		//array.push({Course_name:Cour_name,data:res});
		$.post('http://127.0.0.1:5050/tas_list',{Course_name:disc[i].Course_name,data:array[i]},function(response){
			console.log(response);
		}).	fail(function(){
			alert('Error!!!');
		})

	}
	console.log('successfully selected');
	//alert('successfully selected');
	}
	else if(flag==1)
	{
		alert("Enter correct credentials");
	}
}
function logoutadmin(){
	console.log(123);
	$.post('http://127.0.0.1:5050/logoutadmin',{email:''},function(response){
		//alert('successfully logged out');
		console.log(response);
		window.location.hash='index';
		document.getElementById("email1").value=""
		document.getElementById("pass1").value=""
	}).fail(function(){
		alert('NOT LOGGED OUT');
	})
}
