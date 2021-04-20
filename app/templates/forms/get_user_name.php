<?php

session_start();

if (!isset($_SESSION['loggedIn'])) {
    die;
    }
include("../forms/db_connection.php");   
header('Content-Type: application/json');

$user_id=$_SESSION['user_id'];
$user_name="";
$query_name="SELECT `name` FROM users 
WHERE `id` = '$user_id' ";
$result_name = $connect->query($query_name);
if ($result_name->num_rows > 0) {
        $row = $result_name->fetch_assoc(); 
        $user_name = $row['name'];
       } else{
        var_dump($query_name);
        var_dump($connect->error);
        die; 
       }
          
   
echo json_encode($user_name);
