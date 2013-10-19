<?php
require_once("../inc/head.inc.php");
echo "<h1>Konfiguration</h1>";

if (isset($_POST['smtp_save']) && $_POST['smtp_save'] == 'Speichern') {
$redis->set("config.email.smtp.server",$_POST['smtp_server']);
$redis->set("config.email.smtp.username",$_POST['smtp_username']);
$redis->set("config.email.smtp.password",$_POST['smtp_password']);
$redis->set("config.email.smtp.sender",$_POST['smtp_sender']);
echo "<ul><li>Die Einstellungen wurden erfolgreich gespeichert</li></ul>";
}


$smtp_server = $redis->get("config.email.smtp.server");
$smtp_username = $redis->get("config.email.smtp.username");
$smtp_password = $redis->get("config.email.smtp.password");
$smtp_sender = $redis->get("config.email.smtp.sender");

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



require_once("../inc/foot.inc.php");
?>
