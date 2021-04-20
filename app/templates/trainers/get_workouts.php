<?php

session_start();

if (!isset($_SESSION['trainer']) || $_SESSION['trainer'] == 0) {
     die();
}

include("../forms/db_connection.php");   
header('Content-Type: application/json');

$trainer_id=$_SESSION['user_id'];
$date_from=$_GET['date_from'];
$date_to=$_GET['date_to'];
$query="SELECT `date`,`time`,title, free_slots,`status`,max_participants, trainer_id FROM workouts_timetable 
        LEFT JOIN workout_titles ON workouts_timetable.title_id=workout_titles.id 
        WHERE `date`>='$date_from' AND `date`<= '$date_to' AND trainer_id=$trainer_id";
$result = $connect->query($query);

if (!$result) {
    var_dump($query);
    var_dump($connect->error);
    die;
}

$workouts = [];
if ($result->num_rows > 0) {
    while ($row = $result->fetch_assoc()) {
        //$obj = (object) array('id'=>$row['id'],'name' =>$row["trainer_full_name"]);
        $obj = new stdClass();
        $obj->date = $row['date'];
        $obj->time = $row["time"];
        $obj->title = $row['title'];
        $obj->free_slots = $row["free_slots"];
        $obj->participants=$row['max_participants']-$row["free_slots"];
        $obj->status = $row["status"];

        $workouts[] = $obj;      
    }
}

echo json_encode($workouts);