<?php
require_once("../inc/head.inc.php");

echo "<h1>Konfiguration</h1>";

if (isset($_POST['smtp_save']) && $_POST['smtp_save'] == 'Speichern') {
    $redis->hset("config.email.smtp","server",$_POST['smtp_server']);
    $redis->hset("config.email.smtp","username",$_POST['smtp_username']);
    $redis->hset("config.email.smtp","password",$_POST['smtp_password']);
    $redis->hset("config.email.smtp","sender",$_POST['smtp_sender']);

    echo "<ul><li>Die Einstellungen wurden erfolgreich gespeichert</li></ul>";
}

if (isset($_POST['login_save']) && $_POST['login_save'] == 'Speichern') {
    $login_user   = $_POST["login_user"];
    $login_pass_1 = $_POST["login_pass_1"];
    $login_pass_2 = $_POST["login_pass_2"];
    
    $redis->hset("config.user","username",$login_user);
    $numerrors = 0;
    $errormessage = "";

    if ($login_pass_1 != "") {
        if ($login_pass_1 != $login_pass_2) {
            $numerrors ++;
            $errormessage .= "Die Passwörter sind nicht gleich!<br/>";
        } else {
            $redis->hset("config.user","password",$login_pass_1);
        }
    }
    echo "<ul>";
    echo "<li>Username erfolgreich gespeichert</li>";
    if ($numerrors > 0) echo "<li>$errormessage</li>"; else echo "<li>Passwort erfolgreich gespeichert</li>";
    echo "</ul>";

}


$smtp_server = $redis->hget("config.email.smtp","server");
$smtp_username = $redis->hget("config.email.smtp","username");
$smtp_password = $redis->hget("config.email.smtp","password");
$smtp_sender = $redis->hget("config.email.smtp","sender");
$login_user  = $redis->hget("config.user","username");

echo "<h2>E-Mail-Server</h2>";
echo "Hier werden die Server-Einstellungen für den E-Mail-Versand festgelegt.";
echo "<form action=\"\" method=\"post\">";
echo "<table border=\"0\" cellspacing=\"0\" cellpadding=\"5\">";
echo "<tr><td>Server</td><td><input type=\"text\" name=\"smtp_server\" value = \"$smtp_server\"/></td></tr>";
echo "<tr><td>Username</td><td><input type=\"text\" name=\"smtp_username\" value =\"$smtp_username\"/></td></tr>";
echo "<tr><td>Passwort</td><td><input type=\"password\" name=\"smtp_password\" value =\"$smtp_password\"/></td></tr>";
echo "<tr><td>E-Mail</td><td><input type=\"text\" name=\"smtp_sender\" value = \"$smtp_sender\"/></td></tr>";
echo "<tr><td>&nbsp;</td><td><input type=\"submit\" name=\"smtp_save\" value = \"Speichern\"/></td></tr>";
echo "</table>";
echo "</form>";

echo "<h2>User-Login</h2>";
echo "Hier werden Username und Passwort zum Einloggen in diese Weboberfläche festgelegt";
echo "<form action=\"\" method=\"post\">";
echo "<table border=\"0\" cellspacing=\"0\" cellpadding=\"5\">";
echo "<tr><td>Username</td><td><input type=\"text\" name=\"login_user\" value=\"$login_user\"/></td></tr>";
echo "<tr><td>Passwort</td><td><input type=\"password\" name=\"login_pass_1\"/></td></tr>";
echo "<tr><td>Passwort</td><td><input type=\"password\" name=\"login_pass_2\"/></td></tr>";
echo "<tr><td>&nbsp;</td><td><input type=\"submit\" name=\"login_save\" value=\"Speichern\"/></td></tr>";
echo "</table>";
echo "</form>";

require_once("../inc/foot.inc.php");
?>
