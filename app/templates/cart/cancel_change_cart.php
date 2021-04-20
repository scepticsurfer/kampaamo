<?php

session_start();
if (!isset($_SESSION['loggedIn']) || $_SESSION['admin']==1 || $_SESSION['trainer']==1  ) {
    die;
    }

include("../forms/db_connection.php");

header('Content-Type: application/json');

$result = "false";
$button="";

$user_id = $_SESSION['user_id'];

$product_name = $connect->real_escape_string(strip_tags($_GET['product_name']));
$product_name = filter_var($product_name, FILTER_SANITIZE_STRING);

$product_price = $connect->real_escape_string(strip_tags($_GET['product_price']));
$product_price = filter_var($product_price, FILTER_SANITIZE_STRING);

$quantity = $connect->real_escape_string(strip_tags($_GET['quantity']));
$quantity = filter_var($quantity, FILTER_SANITIZE_STRING);

$button_name = $connect->real_escape_string(strip_tags($_GET['button_name']));
$button_name = filter_var($button_name, FILTER_SANITIZE_STRING);

$query_search= "SELECT id FROM products WHERE product_name='$product_name'";
$result_search = $connect->query($query_search);
if($result_search->num_rows == 0){
    var_dump($query_search);
    var_dump($connect->error);
}else{
    $row = $result_search->fetch_assoc();
    $product_id = $row['id'];

if ($button_name=="POISTA" || $quantity==0){

$query_delete = "DELETE FROM cart WHERE `user_id`='$user_id' AND `product_id`='$product_id'";
$result_delete = $connect->query($query_delete);
if (!$result_delete) {
    var_dump($query_delete);
    var_dump($connect->error);
} else {
    $result = "true";
    $button="delete";
   }
} else{
    $sum_product=$quantity*$product_price;
    $query_update  = "UPDATE cart SET quantity=$quantity, sum_product=$sum_product WHERE `user_id`='$user_id' AND `product_id`='$product_id' ";
    $result_update = $connect->query($query_update);
    if (!$result_update) {
        var_dump($query_update);
        var_dump($connect->error);
    } else {
        $result = "true";
        $button="update";
       } 
   
}
}
$change = new stdClass();
$change->result = $result;
$change->button = $button;

echo json_encode($change);