function validate()
{
	const loginForm = document.getElementById("loginForm");

	loginForm.addEventListener("submit", (e) => {
	e.preventDefault();

	const firstname = document.getElementById("fname").value;
	const lastname = document.getElementById("lname").value;
	const cls = document.getElementById("class").value;

	const formData = new FormData(loginForm);
    const jsonObject = Object.fromEntries(formData);
    const studentinfo = JSON.stringify(jsonObject);

    const request = new XMLHttpRequest()

	if (firstname == "" || lastname == "") 
	{
		alert("Please enter a valid information")
		loginForm.reset()
	} 
	else 
	{
	    //request.open('POST', '/process_student_info/${JSON.stringify(jsonObject)}')
		//alert("Mr./Miss " + firstname + " " + lastname +" belonging to " + cls);
		var xhr = new XMLHttpRequest();
        var url = "/process_student_info";
        xhr.open("POST", url, true);
        xhr.setRequestHeader("Content-Type", "application/json");
        xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            console.log("reached")
            console.log(studentinfo);
            }
        };
        xhr.send(studentinfo);
	}
	})
};