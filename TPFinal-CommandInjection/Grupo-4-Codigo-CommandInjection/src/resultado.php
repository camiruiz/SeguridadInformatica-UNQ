<?php

	$domain_name = $_POST["domain_name"];

	echo nl2br("Hola, el dominio que acabas de buscar es: \n");
	echo system('nslookup '.$domain_name);

?>
