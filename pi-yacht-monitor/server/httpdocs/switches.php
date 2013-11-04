<?php
$section = "i2c";
require_once("../inc/head.inc.php");
echo "<h1>Schalter</h1>";
$keys = $redis->keys("config.i2c.*");
if (isset($_POST["switch"])) {
  $key=$_POST["key"];
  $subkey = $_POST["subkey"];
  $givenvalue = $_POST["givenvalue"];
  $redis->hset($key, $subkey,$givenvalue);
  //avoid double post with reaload
  header("Location:switches.php");
}

echo "<table border='1' cellspacing='0' cellpadding='5'>";
echo "<tr><th>Name</th><th>Output Typ</th><th>Port</th><th>Name</th><th>Istwert</th><th>Sollwert</th><th>Aktion</th></tr>";
foreach ($keys as $key) {
  $v = $redis->hgetall($key);
  $type = $v["type"];
  $name = explode(".",$key)[2];
  if ($type == "PCF8574_OUT_INV") {
    for ($i = 0; $i < 8; $i++) {
       $value = $redis->hget("boat." .$v["in" . $i . "-name"] , "value");
       $givenvalue = $v["in" . $i . "-givenvalue"];
       $text = $value == 0? "an":"aus";
       $newvalue = $value == 0?1:0;
       $subkey = "in" . $i . "-givenvalue";
      
       echo "<form action='' method='post'/>";
       echo "<tr>";
       echo "<td>$name</td>";
       echo "<td>$type</td>";
       echo "<td>$i</td>";
       echo "<td>" . $v["in" . $i . "-name"] . "</td>";
       echo "<td>$value</td>";
       echo "<td>" . $givenvalue . "</td>";
       echo "<td>";
       if ($value != $givenvalue) {
         echo "wird geschaltet";
       } else {
         echo "<input type='submit' name='switch' value='$text'/>";
       }
       echo "<input type='hidden' name='key' value='$key'/>";
       echo "<input type='hidden' name='subkey' value='$subkey'/>";
       echo "<input type='hidden' name='givenvalue' value='$newvalue'/>";
       echo "</td>";
       echo "</tr>";
       echo "</form>";
    }
  } 

}
echo "</table>";
require_once("../inc/foot.inc.php");
?>




