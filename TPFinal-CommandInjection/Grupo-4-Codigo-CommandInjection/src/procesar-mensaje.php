<?php

	$message = $_POST["message"];

    ob_start();
	system('echo ' . $message . ' >> mensajes.txt ');
	ob_end_clean();
	
    echo "<h2>Mensaje recibido</h2>"
?>
