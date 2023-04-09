function validate()
{
	const loginForm = document.getElementById("loginForm");

	loginForm.addEventListener("submit", (e) => {
	e.preventDefault();

	const firstname = document.getElementById("fname").value;
	const lastname = document.getElementById("lname").value;
	const cls = document.getElementById("class").value;

	if (firstname == "" || lastname == "") 
	{
		alert("Please enter a valid information")
		loginForm.reset()
	}
	else
	{

	}

	})
};