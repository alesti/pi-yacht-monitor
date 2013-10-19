<?php
require 'Predis/Autoloader.php';
Predis\Autoloader::register();
$redis = new Predis\Client();


print_r($_POST);
print "Hallo";

if (isset($_POST["login"])) {
  $user = $_POST["username"];
  $pass = $_POST["password"];

  $userdb = $redis->hget("config.user","username");
  $userpass = $redis->hget("config.user","password");

  if ($userdb == "") $userdb = "yacht-monitor";
  if ($userpass =="") $userpass="yacht-monitor";

  if ($user != $userdb || $pass != $userpass) {
     header("Location: login.php");
  } else {
    session_start();
    $_SESSION['login'] = true;
    $_SESSION['user'] = $user;
    header("Location: index.php");
  }
} else {

header("Location: login.php");
}


?>
