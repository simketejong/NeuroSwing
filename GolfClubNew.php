<?php
{

$data = json_decode(file_get_contents('php://input'), true);
//$myfile = fopen("/tmp/Poep_Input.dat", "w") or die("Unable to open file!");
$tekst = implode($data);
$s=$tekst[11];
$a=explode("}", $tekst);
$b=implode($a);
$c=explode("{", $b);
//$d=implode($c);
$groot=count($c, TRUE);

if (empty($s)) {
    $s=0;
}

$file = "/tmp/GolfSwing_Semaphore.lck";

if (!file_exists($file)) {

for ($p = 1; $p < $groot; $p++) {
	$d=$c[$p];
    $e=explode(",", $d);
    $x1=$e[0];
    $x2=explode(":", $x1);
    $y1=$e[1];
    $y2=explode(":", $y1);
    $z1=$e[2];
    $z2=explode(":", $z1);
    //$post='&x='.$x2[1].'&y='.$y2[1].'&z='.$z2[1].'&type='.$s;
    //  fwrite($myfile,$post);
    //fwrite($myfile,$post);


$detect=0;
$vorige=0;
$diff_x_y=($x2[1]-$y2[1])/2000;
$diff_x_z=($x2[1]-$z2[1])/2000;
$diff_y_z=($y2[1]-$z2[1])/2000;

$x_norm=$x2[1]/4000;
$y_norm=$y2[1]/4000;
$z_norm=$z2[1]/4000;


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

if ($s==="2")
{
	$myfile = fopen("/tmp/Test_Input.dat", "w") or die("Unable to open file!");
	//$txt = $x_norm." ".$y_norm." ".$z_norm." ".$diff_x_y." ".$diff_x_z." ".$diff_y_z." ".$_GET["type"]." "."\n";
	$txt = $x_norm." ".$y_norm." ".$z_norm." ".$diff_x_y." ".$diff_x_z." ".$diff_y_z." ".$vorige."\n";
	fwrite($myfile, $txt);
	fclose($myfile);
}
else
{

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
	$txt = $s." ".$detect."\n";
	fwrite($myfile, $txt);
	fclose($myfile);


	$myfile = fopen("/tmp/Previous.dat", "w") or die("Unable to open file!");
	$txt = $s."\n";
	fwrite($myfile, $txt);
	fclose($myfile);
}

$file="/tmp/WegDat.txt";

if (file_exists($file)) 
{
	unlink("/tmp/Output.dat");
	unlink("/tmp/Input.dat");
	unlink("/tmp/Previous.dat");
	//unlink("/tmp/Test_Input.dat");
	sleep(2);
}
}
}

//}
//fclose($myfile);
}
?>