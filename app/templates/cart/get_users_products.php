<?php

session_start();

if (!isset($_SESSION['loggedIn']) || $_SESSION['admin']==1 ||$_SESSION['trainer']==1  ) {
    die;
    }

include("../forms/db_connection.php");   
header('Content-Type: application/json');


$user_id=$_SESSION['user_id'];

$query="SELECT * FROM cart WHERE `user_id`='$user_id'";
$result = $connect->query($query);

if (!$result) {
    var_dump($query);
    var_dump($connect->error);
    die;
}

$user_products = [];
if ($result->num_rows > 0) {
    while ($row = $result->fetch_assoc()) {
        //$obj = (object) array('id'=>$row['id'],'name' =>$row["trainer_full_name"]);
        $product_id=$row['product_id'];
        $query_product="SELECT product_name, `description` FROM products WHERE `id`='$product_id'";
        $result_product = $connect->query($query_product);
        if (!$result_product) {
            var_dump($query);
            var_dump($connect->error);
            die;
        }
        $row_product = $result_product->fetch_assoc();
        $obj = new stdClass();
        $obj->product = $row_product['product_name'];
        $obj->price = $row['price'];
        $obj->quantity = $row['quantity'];
        $obj->sum_product = $row['sum_product'];
        $obj->description = $row_product['description'];
        
        $user_products[] = $obj; 
          
    }
}


echo json_encode($user_products);