<?php

session_start();

if (!isset($_SESSION['admin']) || $_SESSION['admin']!=1) {
    die;
    }
include("../forms/db_connection.php");   
header('Content-Type: application/json');


$title_id=$_GET['title_id'];

$query_trainers="SELECT users.id, users.name FROM trainer_workout_title 
LEFT JOIN users ON trainer_id = users.id WHERE title_id = '$title_id' AND users.trainer = '1'";
$trainers = [];
$result = $connect->query($query_trainers);
if ($result->num_rows > 0) {
    while ($row = $result->fetch_assoc()) {
        $obj = new stdClass();
        $obj->id = $row['id']; 
        $obj->name = $row['name'];
        $trainers[]=$obj;
       }
   
}

echo json_encode($trainers);