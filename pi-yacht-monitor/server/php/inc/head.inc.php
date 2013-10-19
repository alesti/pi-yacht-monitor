<?php
require 'Predis/Autoloader.php';
Predis\Autoloader::register();
$redis = new Predis\Client();
session_start();

if (!isset($_SESSION['login']) || $_SESSION['login'] != true) {
  header("Location: login.php");
}

?>
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN">
<html>
<head>
<meta http-equiv="content-type" content="text/html; charset=utf-8">
<title>Yacht-Monitor</title>
<link rel="stylesheet" type="text/css" href="css/layout.css">
</head>
<body>
<div id="navi">
<ul>
<li><a href="index.php">Startseite</a></li>
<li><a href="webcam.php">Webcam</a></li>
<li><a href="config.php">Konfiguration</a></li>
<li><a href="collectors.php">Sensoren</a></li>
<li><a href="info.php">Info</a></li>
<li><a href="logout.php">Logout</a></li>
</ul>
</div>
<div id="content">

