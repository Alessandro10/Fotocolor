<?php
	$myfile = fopen("LOG_FILE2.txt", "a") or die("Unable to open file!");
	$txt = "Altro Mouse\n";
	fwrite($myfile, $txt);
	$txt = "Minnie Mouse\n";
	fwrite($myfile, $txt);
	fclose($myfile);
?>