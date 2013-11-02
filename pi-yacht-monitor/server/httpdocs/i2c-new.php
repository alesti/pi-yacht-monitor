<?php
$section="i2c";

require_once("./i2c/PCF8591.php");
require_once("./i2c/PCF8574_IN.php");
require_once("../inc/head.inc.php");

if (!isset($_GET['step'])) {
  $step = 1;
} else {
  $step = $_GET['step'];
}

echo "<h1>Neue I2C-Komponente hinzufügen</h1>";

if  ($step == 1) {
  echo "<form method=\"post\" action=\"?step=2\">";
  echo '<table border="0" cellspacing="0" cellpadding="5">';
  echo '<tr><td>Typ:</td><td>';
  echo '<select name="type">';
  echo '<option value="">Bitte auswählen...</option>';
  echo '<option value="PCF8591">A/D Wandler PCF8591</option>';
  echo '<option value="LM75">Temperatursensor LM75</option>';
  echo '<option value="PCF8574_IN">Digital input PCF8574</option>';
  echo '</select></td></tr>';
  echo '<tr><td>Name</td><td><input type="text" name="name"/></td></tr>';
  echo '<tr><td>Bus</td><td><input type="text" name="bus" value="1"/></td></tr>';
  echo '<tr><td>Adresse</td><td><input type="text" name="address"/></td></tr>';
  echo '<tr><td>Aktiv</td><td><input type="checkbox" name="active" value="active" checked/></td></tr>';
  echo '<tr><td>&nbsp;</td><td><input type="submit" name="weiter" value="weiter"/></tr></td>';
  echo '</table>';
  echo "</form>";
} else if ( $step == 2) {
  $type= $_POST["type"];
  $bus= $_POST["bus"];
  $address = $_POST["address"];
  $active = isset($_POST["active"])?1:0;
  $name = $_POST["name"];
  
  if ($type == "PCF8591") {
    $mod = new PCF8591;
    $mod->bus = $bus;
    $mod->address = $address;
    $mod->active = $active;
    $mod->name = $name;
    $mod->type = $type;
    echo $mod->getNewForm("?step=3");
  } else if ($type == "LM75") {
    if (!$redis->exists("config.i2c.$name")) {
      $key = "config.i2c.$name";
      $redis->hset($key,"active",$active);
      $redis->hset($key,"type",$type);
      $redis->hset($key,"bus",$bus);
      $redis->hset($key,"address",$address);
      $redis->hset($key,"name",$name);
      echo "Erfolgreich gepeichert";
    } else {
      echo "Nicht gespeichert. Name schon vorhanden!";
    }
  } else if ($type == "PCF8574_IN") {
      $mod = new PCF8574_IN;
      $mod->bus = $bus;
      $mod->address = $address;
      $mod->active = $active;
      $mod->name=$name;
      $mod->type=$type;
      echo $mod->getNewForm("?step=3");
  }


} else if ($step == 3) {
  $type = $_POST["type"];
  if ($type == "PCF8591") {
    $in0active = isset($_POST["in-0-active"])?1:0; $in0name   = $_POST["in-0-name"]; $in0factor = $_POST["in-0-factor"]; 
    $in1active = isset($_POST["in-1-active"])?1:0; $in1name   = $_POST["in-1-name"]; $in1factor = $_POST["in-1-factor"]; 
    $in2active = isset($_POST["in-2-active"])?1:0; $in2name   = $_POST["in-2-name"]; $in2factor = $_POST["in-2-factor"]; 
    $in3active = isset($_POST["in-3-active"])?1:0; $in3name   = $_POST["in-3-name"]; $in3factor = $_POST["in-3-factor"];
    $address = $_POST["address"]; 
    $bus = $_POST["bus"]; 
    $active = $_POST["active"];
    $name = $_POST["name"];
    if (!$redis->exists("config.i2c.$name")) {
      $key = "config.i2c.$name";
      $redis->hset($key,"active",$active);
      $redis->hset($key,"type",$type);
      $redis->hset($key,"bus",$bus);
      $redis->hset($key,"address",$address);
      $redis->hset($key,"in0-active",$in0active); $redis->hset($key,"in0-name",$in0name); $redis->hset($key,"in0-factor",$in0factor);
      $redis->hset($key,"in1-active",$in1active); $redis->hset($key,"in1-name",$in1name); $redis->hset($key,"in1-factor",$in1factor);
      $redis->hset($key,"in2-active",$in2active); $redis->hset($key,"in2-name",$in2name); $redis->hset($key,"in2-factor",$in2factor);
      $redis->hset($key,"in3-active",$in3active); $redis->hset($key,"in3-name",$in3name); $redis->hset($key,"in3-factor",$in3factor);
      echo "Erfolgreich gespeichert";
    } else {
      echo "Nicht gespeichert, Name existiert schon!";
    }
  } else if ($type == "PCF8574_IN") {
      $in0active = isset($_POST["in-0-active"])?1:0; $in0name = $_POST["in-0-name"];
      $in1active = isset($_POST["in-1-active"])?1:0; $in1name = $_POST["in-1-name"];
      $in2active = isset($_POST["in-2-active"])?1:0; $in2name = $_POST["in-2-name"];
      $in3active = isset($_POST["in-3-active"])?1:0; $in3name = $_POST["in-3-name"];
      $in4active = isset($_POST["in-4-active"])?1:0; $in4name = $_POST["in-4-name"];
      $in5active = isset($_POST["in-5-active"])?1:0; $in5name = $_POST["in-5-name"];
      $in6active = isset($_POST["in-6-active"])?1:0; $in6name = $_POST["in-6-name"];
      $in7active = isset($_POST["in-7-active"])?1:0; $in7name = $_POST["in-7-name"];
      $address = $_POST["address"]; 
      $bus = $_POST["bus"];
      $active = $_POST["active"];
      $name = $_POST["name"];
      $key = "config.i2c.$name";
      $redis->hset($key,"active",$active);
      $redis->hset($key,"type",$type);
      $redis->hset($key,"bus",$bus);
      $redis->hset($key,"address",$address);
      $redis->hset($key,"in0-active",$in0active); $redis->hset($key,"in0-name",$in0name);
      $redis->hset($key,"in1-active",$in1active); $redis->hset($key,"in1-name",$in1name);
      $redis->hset($key,"in2-active",$in2active); $redis->hset($key,"in2-name",$in2name);
      $redis->hset($key,"in3-active",$in3active); $redis->hset($key,"in3-name",$in3name);
      $redis->hset($key,"in4-active",$in4active); $redis->hset($key,"in4-name",$in4name);
      $redis->hset($key,"in5-active",$in5active); $redis->hset($key,"in5-name",$in5name);
      $redis->hset($key,"in6-active",$in6active); $redis->hset($key,"in6-name",$in6name);
      $redis->hset($key,"in7-active",$in7active); $redis->hset($key,"in7-name",$in7name);
      echo "Erfolgreich gespeichert";
  }
}









require_once("../inc/foot.inc.php");
?>




