console.log("Javascript loaded")

inputField = document.getElementById("input");
submit = document.getElementById("tab-click");
inputField.focus();

//submit form when 'Enter' key is pressed
inputField.addEventListener("keyup", function(event) {
    if (event.keyCode === 17) {
		submit.click();
        return false;
    }
});



$(document).ready(function() {

	$('form').on('submit', function(event) {

		$.ajax({
			data : {
				command : $('#input').val(),
			},
			type : 'POST',
			url : '/enter'
		})

		.done(function(data) {
			window.document.location.href = "http://127.0.0.1:5000";
		});

		event.preventDefault();
	});


	$('#tab-click').on('click', function (event) {
		$.ajax({
			data : {
				command : $('#input').val(),
			},
			type: 'POST',
			url : '/tab'
		})

		.done(function(data) {
			console.log("ge")
			if (data.error) {
				$('#input').val("error");
			}
			else {
				$('#input').val("asd");
			}

		});
		event.preventDefault();
	});

});