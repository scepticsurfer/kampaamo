<?php

session_start();

if (!isset($_SESSION['loggedIn']) || $_SESSION['admin']==1 || $_SESSION['trainer']==1  ) {
    die;
    }

include("../forms/db_connection.php");   
header('Content-Type: application/json');

$user_id=$_SESSION['user_id'];
$date_from=$_GET['date_from'];
$date_to=$_GET['date_to'];
$query="SELECT `date`,`time`,title,`name` FROM workouts_registration 
        LEFT JOIN workout_titles ON workouts_registration.title_id=workout_titles.id 
        LEFT JOIN users ON workouts_registration.trainer_id=users.id
        WHERE participant_id='$user_id' AND `date`>='$date_from' AND `date`<= '$date_to'";
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
        $obj->trainer = $row["name"];
        
        $workouts[] = $obj; 
          
    }
}

echo json_encode($workouts);