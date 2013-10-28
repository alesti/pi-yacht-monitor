<?php
require_once("../inc/head.inc.php");

if (!isset($_GET['step'])) {
  $step = 1;
} else {
  $step = $_GET['step'];
}

echo "<h1>Neue I2C-Komponente hinzufügen</h1>";

if  ($step == 1) {
  echo '<table border="0" cellspacing="0" cellpadding="5">';
  echo '<tr><td>Typ:</td><td>';
  echo '<select name="typ">';
  echo '<option value="">Bitte auswählen...</option>';
  echo '<option value="PCF8591">A/D Wandler PCF8591</option>';
  echo '<option value="LM75">Temperatursensor LM75</option>';
  echo '</select></td></tr>';
  echo '<tr><td>Bus</td><td><input type="text" name="bus" value="1"/></td></tr>';
  echo '<tr><td>Adresse</td><td><input type="text" name="address"/></td></tr>';
  echo '<tr><td>Aktiv</td><td><input type="checkbox" name="active" value="active" checked/></td></tr>';
  echo '<tr><td>&nbsp;</td><td><input type="submit" name="weiter" value="weiter"/></tr></td>';
  echo '</table>';
}









require_once("../inc/foot.inc.php");
?>




