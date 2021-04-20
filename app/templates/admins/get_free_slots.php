<?php
session_start();

if (!isset($_SESSION['admin']) || $_SESSION['admin']!=1) {
    die;
    }

include("../forms/db_connection.php");   
header('Content-Type: application/json');

$title_id=$_GET['title_id'];
$workout_id=$_GET['workout_id'];


if ($workout_id==""){

$query_free_slots="SELECT max_participants FROM workout_titles 
WHERE id = '$title_id' ";

$result = $connect->query($query_free_slots);
if ($result->num_rows > 0) {
        $row = $result->fetch_assoc();
         
       $slots=$row['max_participants'];
} else{
    var_dump($query_free_slots);
    var_dump($connect->error);
    die;
}  
} else{
    $query_free_slots="SELECT free_slots FROM workouts_timetable
    WHERE workout_id ='$workout_id' "; 

    $result = $connect->query($query_free_slots);
    if ($result->num_rows > 0) {
        $row = $result->fetch_assoc();
        $slots=$row['free_slots']; 
    }  else{
        var_dump($query_free_slots);
        var_dump($connect->error);
        die;
    }   
}

echo json_encode($slots);