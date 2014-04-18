<?php
/* ERROR REPORTING */
error_reporting(E_ALL);
ini_set('display_errors', 1);  


session_start();
if (!isset($section)) $section = "";
require 'Predis/Autoloader.php';
Predis\Autoloader::register();
$redis = new Predis\Client();
require_once("lang.php");

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
<li><a href="index.php"><?php echo $lang['MENU_HOME']; ?></a></li>
<li><a href="switches.php"><?php echo $lang['MENU_SWITCH']; ?></a></li>
<li><a href="config.php"><?php echo $lang['MENU_CONFIG']; ?></a></li>
<li><a href="monitoring.php"><?php echo $lang['MENU_MONITORING'];?></a></li>
<li><a href="i2c.php"><?php echo $lang['MENU_I2CCONFIG']; ?></a>
<?php
 if ($section == 'i2c') {
   echo "<ul class='sub'><li><a href='i2c-new.php'>".$lang['MENU_NEW']."</a></li></ul>";
 }
?>
</li>
<li><a href="info.php"><?php echo $lang['MENU_INFO']; ?></a></li>
<li><a href="logout.php"><?php echo $lang['MENU_LOGOUT']; ?></a></li>
</ul>
</div>
<div id="content">

