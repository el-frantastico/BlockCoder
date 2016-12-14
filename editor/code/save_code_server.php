
<?php
	header('Content-type: text/html; charset=utf-8');

	$dir = 'upload';

	if( !file_exists($dir)) {
		$oldmask = umask(0);
		mkdir ($dir, 0777);
	}
	
	if(!empty($_POST['data'])) {
		$data = $_POST['data'];
		$fname = "usercode.py";
		
		$file = fopen($dir.'/'.$fname, 'w');
		fwrite($file, $data);
		fclose($file);
	}

	// $python = 'python /var/www/html/blockcoder/editor/code/upload/test.py'
	// echo $python
	//system('python /var/www/html/blockcoder/editor/code/upload/test.py');
    //system('sudo python /var/www/html/blockcoder/editor/code/upload/usercode.py');
    //exec('./script.sh');
    $old_path = getcwd();
    chdir('/var/www/html/blockcoder/editor/code/upload');
    exec('bash script.sh');
    chdir($old_path);
?>

	
