var courses=function() {
	var arr=["ITWS2","DS","MATHS2","BEC","CSO","HSS"];
	var n=arr.length;
	var i;
	var str="<option>"+"select a course"+"</option>"
	for(i=0;i<n;i++)
	{
		str=str+"<option value=" + arr[i] + ">" + arr[i] + "</option>"
	}
	document.getElementById("lcourses1").innerHTML=str
	document.getElementById("lcourses2").innerHTML=str
	document.getElementById("lcourses3").innerHTML=str
	
};
/*var addNewStudentResponse;
function back1(){
		courses();
	$.ajax({
		url:'http://127.0.0.1:5050/addStudent',
		method: 'POST',
		data:{
			"roll":$("#roll2").value,
			"name":$("#name2").value,
			"email":$("#email2").value,
			"password":$("#pass2").value,
			"year":$("#year2").value,
			"CGPA":$("#cgpa2").value,
			"Course_priority1":$("#Course_priority1").value,
			"Course_priority2":$("#Course_priority2").value,
			"Course_priority3":$("#Course_priority3").value,
		},
		async:false,//false
		success: function (response) {
			console.log(response);
			addNewStudentResponse=response;
                alert(response);
            },
       	error: function (response) {
       		console.log(response);
            addNewStudentResponse=response;
              	alert(addNewStudentResponse.responseText);
            }
	}),
	window.location.hash='index';
}*/
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
			Course_priority3:$("#lcourses3").find(":selected").text()},function(data){
				alert(data);
				console.log(data);
			}).fail(function(){
				alert('Error!!!');
			});
			return ret;

};