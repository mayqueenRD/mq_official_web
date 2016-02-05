<?php 
session_start(); 

$alphanum = "ABCDEFGHJKLMNPQRSTUVWXYZ23456789";

// generate the verication code
$rand = substr(str_shuffle($alphanum), 0, 5); 
$_SESSION["vercode"] = $rand; 
$height = 25; 
$width = 65; 
 
$image_p = imagecreate($width, $height); 
$black = imagecolorallocate($image_p, 0, 0, 0); 
$white = imagecolorallocate($image_p, 255, 255, 255); 
$font_size = 14; 
 
imagestring($image_p, $font_size, 5, 5, $rand, $white); 
imagejpeg($image_p, null, 80); 
?>