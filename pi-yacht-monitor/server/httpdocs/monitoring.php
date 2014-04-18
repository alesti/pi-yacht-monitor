<?php
require_once("../inc/head.inc.php");
echo "<h1>Monitoring</h1>";


echo "<h2>Überwachte Werte</h2>";
$keys = $redis->keys("config.monitor.*");

echo "<table border=\"1\" cellspacing=\"0\" cellpadding=\"5\">";
foreach($keys as $key) {
 $row = $redis->hgetall($key);
 echo "<tr>";
  echo "<td>" . $row["name"] . "</td>";
  echo "<td>" . $row["min"] . "</td>";
  echo "<td>" . $row["max"] . "</td>";
 echo "</tr>";
}
echo "</table>";

$keys = $redis->keys("boat.*");

echo "<table border=\"1\" cellspacing=\"0\" cellpadding=\"5\">"; 

foreach ($keys as $key) {

  $row = $redis->hgetall($key);
  echo "<tr>";
  echo "<td>" . explode(".",$key)[1] . "</td>"; 
  echo "<td>" . $row["value"] . "</td>";
  echo "<td>" . date("d.m.Y H:i:s",$row["time"]) . "</td>";
  echo "</tr>";
}

echo "</table>";

require_once("../inc/foot.inc.php");
?>
