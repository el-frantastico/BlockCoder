function run() {
	var a = document.createElement('a');
  	a = document.getElementById('content_python').innerHTML.toString();
	 
	save_to_server(a);
}

function save_to_server(code) {
	var data = new FormData();
	data.append("data", code);
	var xhr = new XMLHttpRequest();
	xhr.open( 'post', './save_code_server.php', true );
	xhr.send(data);
	// 	xhr.timeout = 2500;	
	// setTimeout(function() {
	// 	var xhr2 = new XMLHttpRequest();
	// 	xhr2.open( 'post', './compile_python_server.php', true);
	// 	xhr2.send();
	// }, 2500);
	
}

function compile_code() {
	var xhr = new XMLHttpRequest();
	xhr.open( 'post', './compile_python_server.php', true);
	xhr.send();
}
