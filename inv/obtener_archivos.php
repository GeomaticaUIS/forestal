<?php
$archivos = glob('*.html'); // Obtiene todos los archivos HTML en el directorio actual

$response = array();
foreach ($archivos as $archivo) {
  $response[] = $archivo;
}

echo json_encode($response);
?>
