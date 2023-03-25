function validate()
{
	const demoForm = document.getElementById("demographicForm");

	loginForm.addEventListener("submit", (e) => {
	e.preventDefault();

	//const firstname = document.getElementById("fname").value;
	//const lastname = document.getElementById("lname").value;
	//const cls = document.getElementById("class").value;

	const formData = new FormData(demoForm);
    const jsonObject = Object.fromEntries(formData);
    const demoinfo = JSON.stringify(jsonObject);

    const request = new XMLHttpRequest()

	/*if (firstname == "" || lastname == "")
	{
		alert("Please enter a valid information")
		loginForm.reset()
	}*/
	    //request.open('POST', '/process_student_info/${JSON.stringify(jsonObject)}')
		//alert("Mr./Miss " + firstname + " " + lastname +" belonging to " + cls);
		var xhr = new XMLHttpRequest();
        var url = "/process_student_demographic_info";
        xhr.open("POST", url, true);
        xhr.setRequestHeader("Content-Type", "application/json");
        xhr.onreadystatechange = function () {
        if (xhr.readyState === 4 && xhr.status === 200) {
            console.log("reached")
            console.log(demoinfo);
            }
        };
        xhr.send(demoinfo);
	})
};