<?php
require_once("I2C.php");

class PCF8591 extends I2C{
  public $port0active;
  public $port0name;
  public $port0factor;
  public $port1active;
  public $port1name;
  public $port1factor;
  public $port2active;
  public $port2name;
  public $port2factor;
  public $port3active;
  public $port3name;
  public $port3factor;

  public function getNewForm($action) {
    $res = "";
    $res .= "<form method=\"post\" action=\"?step=3\">";
    $res .= "<table border=\"0\" cellspacing=\"0\" cellpadding=\"5\">";
    $res .= "<tr><th>Port</th><th>Aktiv</th><th>Name</th><th>Faktor</th></tr>";
    $res .= "<tr><td>1</td><td><input name=\"in-0-active\" type=\"checkbox\"/></td><td><input name=\"in-0-name\" type=\"text\"/></td><td><input name=\"in-0-factor\" type=\"text\"></td></tr>";
    $res .= "<tr><td>2</td><td><input name=\"in-1-active\" type=\"checkbox\"/></td><td><input name=\"in-1-name\" type=\"text\"/></td><td><input name=\"in-1-factor\" type=\"text\"></td></tr>";
    $res .= "<tr><td>3</td><td><input name=\"in-2-active\" type=\"checkbox\"/></td><td><input name=\"in-2-name\" type=\"text\"/></td><td><input name=\"in-2-factor\" type=\"text\"></td></tr>";
    $res .= "<tr><td>4</td><td><input name=\"in-3-active\" type=\"checkbox\"/></td><td><input name=\"in-3-name\" type=\"text\"/></td><td><input name=\"in-3-factor\" type=\"text\"></td></tr>";
    $res .= "<tr><td>&nbsp;</td><td>&nbsp;</td><td><input type=\"submit\" name=\"speichern\" value=\"speichern\"/></td><td>";
    $res .= "<input type=\"hidden\" name=\"type\" value=\"$this->type\"/>";
    $res .= "<input type=\"hidden\" name=\"bus\" value=\"$this->bus\"/>";
    $res .= "<input type=\"hidden\" name=\"active\" value=\"$this->active\"/>";
    $res .= "<input type=\"hidden\" name=\"name\" value=\"$this->name\"/>";
    $res .= "<input type=\"hidden\" name=\"address\" value=\"$this->address\"/>";
    $res .= "</td></tr>";
    $res .= "</table>";
    $res .= "</form>";
    return $res;
  }
}


?>
