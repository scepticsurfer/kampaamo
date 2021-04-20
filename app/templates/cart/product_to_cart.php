<?php

session_start();


if (isset($_SESSION['admin']) && $_SESSION['admin'] == 1 || isset($_SESSION['trainer'])&& $_SESSION['trainer'] == 1) {
    die;
}

include("../forms/db_connection.php");

header('Content-Type: application/json');

$product_name = $connect->real_escape_string(strip_tags($_GET['product_name']));
$product_name = filter_var($product_name, FILTER_SANITIZE_STRING);

$result = "false";
$registration = "false";

if (isset($_SESSION['user_id'])) {
    $registration = "true";
    $user_id = $_SESSION['user_id'];

    $query_check = "SELECT id, price FROM products WHERE product_name='$product_name'";
    $result_check = $connect->query($query_check);

    if ($result_check->num_rows > 0) {
        $row = $result_check->fetch_assoc();
        $product_price = $row['price'];
        $product_id = $row['id'];
        $query_cart = "SELECT quantity, sum_product FROM cart WHERE `user_id`=$user_id AND product_id=$product_id";
        $result_cart = $connect->query($query_cart);
        if ($result_cart->num_rows > 0) {
            $row_cart = $result_cart->fetch_assoc();
            $quantity = $row_cart['quantity'] + 1;
            $sum_product = $row_cart['sum_product'] + $product_price;
            $query_update = "UPDATE cart SET quantity='$quantity', sum_product='$sum_product' WHERE`user_id`=$user_id AND product_id=$product_id ";
            $result_update = $connect->query($query_update);
            if (!$result_update) {
                var_dump($query_insert);
                var_dump($connect->error);
            } else {
                $result = "true";
            }
        } else {
            $query_insert = "INSERT INTO cart(`user_id`,product_id,price,quantity,sum_product) 
                            VALUES ('$user_id','$product_id','$product_price','1','$product_price')";
            $result_insert = $connect->query($query_insert);

            if (!$result_insert) {
                var_dump($query_insert);
                var_dump($connect->error);
            } else {
                $result = "true";
            }
        }
    } else {
        var_dump($query_check);
        var_dump($connect->error);
    }
}
$result_add = new stdClass();
$result_add->result = $result;
$result_add->registration = $registration;

echo json_encode($result_add);
