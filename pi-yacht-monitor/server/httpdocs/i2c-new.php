<?php
$section="i2c";

require_once("./i2c/PCF8591.php");
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
  } else if ($type = "LM75") {
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
    
  }


} else if ($step == 3) {
  $in0active = isset($_POST["in-0-active"])?1:0;
  $in0name   = $_POST["in-0-name"]; 
  $in0factor = $_POST["in-0-factor"]; 
  $in1active = isset($_POST["in-1-active"])?1:0;
  $in1name   = $_POST["in-1-name"]; 
  $in1factor = $_POST["in-1-factor"]; 
  $in2active = isset($_POST["in-2-active"])?1:0;
  $in2name   = $_POST["in-2-name"]; 
  $in2factor = $_POST["in-2-factor"]; 
  $in3active = isset($_POST["in-3-active"])?1:0;
  $in3name   = $_POST["in-3-name"]; 
  $in3factor = $_POST["in-3-factor"];
  $address = $_POST["address"]; 
  $type = $_POST["type"]; 
  $bus = $_POST["bus"]; 
  $active = $_POST["active"];
  $name = $_POST["name"];

  if (!$redis->exists("config.i2c.$name")) {
    $key = "config.i2c.$name";

    $redis->hset($key,"active",$active);
    $redis->hset($key,"type",$type);
    $redis->hset($key,"bus",$bus);
    $redis->hset($key,"address",$address);
    $redis->hset($key,"in0-active",$in0active);
    $redis->hset($key,"in0-name",$in0name);
    $redis->hset($key,"in0-factor",$in0factor);
    $redis->hset($key,"in1-active",$in1active);
    $redis->hset($key,"in1-name",$in1name);
    $redis->hset($key,"in1-factor",$in1factor);
    $redis->hset($key,"in2-active",$in2active);
    $redis->hset($key,"in2-name",$in2name);
    $redis->hset($key,"in2-factor",$in2factor);
    $redis->hset($key,"in3-active",$in3active);
    $redis->hset($key,"in3-name",$in3name);
    $redis->hset($key,"in3-factor",$in3factor);
    echo "Erfolgreich gespeichert";
  } else {
    echo "Nicht gespeichert, Name existiert schon!";
  }





}









require_once("../inc/foot.inc.php");
?>




