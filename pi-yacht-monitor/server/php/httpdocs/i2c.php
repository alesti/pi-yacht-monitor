<?php
$section = "i2c";
require_once("../inc/head.inc.php");
echo "<h1>I2C-Komponenten</h1>";
$keys = $redis->keys("config.i2c.*");

echo "<table border='1' cellspacing='0' cellpadding='5'>";
echo "<tr><th>Name</th><th>Type</th><th>Bus</th><th>Address</th><th>Active</th></tr>";
foreach ($keys as $key) {
  $v = $redis->hgetall($key);
  echo "<tr>";
  echo "<td>" . explode(".",$key)[2] . "</td>";
  echo "<td>" . $v["type"] .  "</td>";
  echo "<td>" . $v["bus"] . "</td>";
  echo "<td>" . $v["address"] . "</td>";
  echo "<td>".$v["active"]."</td>";

}
echo "</table>";
echo "Hier sollte der output von i2cdetect stehen. Ist das nicht der Fall, dann muss in der php.ini der pfad '/usr/sbin' in den include_path eingetragen werden. Danach apache2 reload";
echo "<br/><br/>i2cdetect -y 0";
echo "<pre>";
echo shell_exec("/usr/sbin/i2cdetect -y 0");
echo "</pre>";
echo "<br/><br/>i2cdetect -y 1";
echo "<pre>";
echo shell_exec("/usr/sbin/i2cdetect -y 1");
echo "</pre>";
require_once("../inc/foot.inc.php");
?>




