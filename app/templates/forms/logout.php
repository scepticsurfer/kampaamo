<?php
include('./db_connection.php');
session_start();
session_unset();
session_destroy();
if ($_COOKIE['user_id']){
$user_id=$_COOKIE['user_id'];
$query="UPDATE users_tokens SET token_cookie=NULL, cookie_expiry=NULL WHERE user_id='$user_id' ";
$result=$connect->query($query);
setcookie("user_id","", time() - 3600, "/");
setcookie("token_cookie","", time() - 3600, "/");
setcookie("expiry_date", "", time() - 3600, "/");
}

header("location:login.php");

exit();
?>