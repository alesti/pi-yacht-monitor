<?php
require_once("../inc/head.inc.php");
echo "<h1>Sensoren</h1>";
$keys = $redis->keys("collector.*");
echo "Folgende Sensor-Scripte sind installiert und werden ausgeführt:";

echo "<table border='1' cellspacing='0' cellpadding='5'>";
echo "<tr><th>Name</th><th>Script</th><th>Params</th><th>Interval</th><th>Lastun</th></tr>";
foreach ($keys as $key) {
  $v = $redis->hgetall($key);
  echo "<tr>";
  echo "<td>" . explode(".",$key)[1] . "</td>";
  echo "<td>" . $v["script"] .  "</td>";
  echo "<td>" . $v["params"] . "</td>";
  echo "<td>".$v["interval"]."</td>";
  echo "<td>".date("d.m.Y H:i:s",$v["lastrun"])."</td></tr>";
}
echo "</table>";

require_once("../inc/foot.inc.php");
?>




