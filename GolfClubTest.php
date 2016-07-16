<?php
{
// &x='+e.accel.x+'&y='+e.accel.y+'&z='+e.accel.z+'&vibe='+e.accel.vibe+'&time='+e.accel.time+'&long='+myLong+'&lat='+myLat+'&type='+SwingType

$diff_x_y=($_GET["x"]-$_GET["y"])/2000;
$diff_x_z=($_GET["x"]-$_GET["z"])/2000;
$diff_y_z=($_GET["y"]-$_GET["z"])/2000;

$x_norm=$_GET["x"]/4000;
$y_norm=$_GET["y"]/4000;
$z_norm=$_GET["z"]/4000;

$myfile = fopen("/tmp/Test_Input.dat", "w") or die("Unable to open file!");
//$txt = $x_norm." ".$y_norm." ".$z_norm." ".$diff_x_y." ".$diff_x_z." ".$diff_y_z." ".$_GET["type"]." "."\n";
$txt = $x_norm." ".$y_norm." ".$z_norm." ".$diff_x_y." ".$diff_x_z." ".$diff_y_z." "."\n";
fwrite($myfile, $txt);
fclose($myfile);
}
?>