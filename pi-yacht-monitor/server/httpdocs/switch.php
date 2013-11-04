<?php
#$section="i2c";
require_once("../inc/head.inc.php");

$name="IOInvers";

echo "<b>Port Management</b></br>";
echo "<b>Device ".$name."</b>";
echo "</br></br>";

      $key = "config.i2c.$name";
      $active=$redis->hget($key,"active");
      $type=$redis->hget($key,"type");
      $bus=$redis->hget($key,"bus");
      $address=$redis->hget($key,"address");
      $name=$redis->hget($key,"name");

echo "<form action='switch.php'>";	  
echo "<table border='1'>";	  
echo "<tr><th>Port</th><th>Aktiv</th><th>Einschalten</th><th>Beschreibung</th>";
	  
	   for($i=0; $i < 8; $i++)
    {
	    $active="";
		$inname="in".$i."-name";
		$inactive="in".$i."-active";
		echo "<tr>";
		echo "<td valign='middle' align='center'>".$i."</td>";
		$active=$redis->hget($key,$inactive);
		if ($active==0) {
				echo "<td valign='middle' align='center'><input type='checkbox' name=$inactive value='1'></td>";
				}else{
				echo "<td valign='middle' align='center'><input type='checkbox' name=$inactive value='1' checked></td>";
		}
	    $key2="boat.". $redis->hget($key,$inname);
		$register=$redis->hget($key2,"value");
		if ($register==0) {
				echo "<td valign='middle' align='center'><input type='checkbox' name=$register value='1'></td>";
				}else{
				echo "<td valign='middle' align='center'><input type='checkbox' name=$register value='1' checked></td>";
		}
	
		echo "<td valign='left' align='left'>". $redis->hget($key,$inname);"</td>";
		echo "</tr>";
    }
echo "</table>";	














require_once("../inc/foot.inc.php");
?>