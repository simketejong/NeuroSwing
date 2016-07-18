<?php
{
// &x='+e.accel.x+'&y='+e.accel.y+'&z='+e.accel.z+'&vibe='+e.accel.vibe+'&time='+e.accel.time+'&long='+myLong+'&lat='+myLat+'&type='+SwingType

$detect=0;
$vorige=0;
$diff_x_y=($_GET["x"]-$_GET["y"])/2000;
$diff_x_z=($_GET["x"]-$_GET["z"])/2000;
$diff_y_z=($_GET["y"]-$_GET["z"])/2000;

$x_norm=$_GET["x"]/4000;
$y_norm=$_GET["y"]/4000;
$z_norm=$_GET["z"]/4000;

$file = "/tmp/Previous.dat";

if (file_exists($file)) {
	$myfile = fopen("/tmp/Previous.dat", "r") or die("Unable to open file!");
	$vorige=fgetc($myfile);
	fclose($myfile);
}
else
{
	$vorige=0;
}

$myfile = fopen("/tmp/Input.dat", "a") or die("Unable to open file!");
//$txt = $x_norm." ".$y_norm." ".$z_norm." ".$diff_x_y." ".$diff_x_z." ".$diff_y_z." ".$_GET["type"]." "."\n";
$txt = $x_norm." ".$y_norm." ".$z_norm." ".$diff_x_y." ".$diff_x_z." ".$diff_y_z." ".$vorige."\n";
fwrite($myfile, $txt);
fclose($myfile);


if ($vorige==="1")
{
	if ($_GET["type"]==="0")
	{
		$detect=1;
	}
	else
	{
		$detect=0;
	}
$myfile = fopen("/tmp/SwingInput.dat", "a") or die("Unable to open file!");
$txt = $x_norm." ".$y_norm." ".$z_norm." ".$diff_x_y." ".$diff_x_z." ".$diff_y_z." ".$vorige."\n";
fwrite($myfile, $txt);
fclose($myfile);

$myfile = fopen("/tmp/SwingOutput.dat", "a") or die("Unable to open file!");
$txt = $_GET["type"]." ".$detect."\n";
fwrite($myfile, $txt);
fclose($myfile);
}

$myfile = fopen("/tmp/Output.dat", "a") or die("Unable to open file!");
$txt = $_GET["type"]." ".$detect."\n";
fwrite($myfile, $txt);
fclose($myfile);


$myfile = fopen("/tmp/Previous.dat", "w") or die("Unable to open file!");
$txt = $_GET["type"]."\n";
fwrite($myfile, $txt);
fclose($myfile);
}
$file="/tmp/WegDat.txt";

if (file_exists($file)) {
unlink("/tmp/Output.dat");
unlink("/tmp/Input.dat");
unlink("/tmp/Previous.dat");
}
?>