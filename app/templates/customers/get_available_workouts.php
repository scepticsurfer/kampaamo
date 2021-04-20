<?php

session_start();

if (!isset($_SESSION['loggedIn']) || $_SESSION['admin']==1 ||$_SESSION['trainer']==1  ) {
    die;
    }

include("../forms/db_connection.php");   
header('Content-Type: application/json');

//$user_id=$_SESSION['user_id'];
$date_from=$_GET['date_from'];
$date_to=$_GET['date_to'];
$trainer_id=$_GET['trainer'];
$workout_id=$_GET['workout'];
$query_part="";
if($trainer_id!="" && $workout_id!=""){
     $query_part=" AND ((trainer_id='$trainer_id') AND (title_id='$workout_id')) ";
    }elseif($workout_id!="" ){
        $query_part=" AND (title_id='$workout_id') ";
    }elseif($trainer_id!=""){
        $query_part=" AND (trainer_id='$trainer_id') ";
    }


$query="SELECT `date`,`time`,title,`name`,free_slots,workout_id,title_id, trainer_id FROM workouts_timetable
        LEFT JOIN workout_titles ON workouts_timetable.title_id=workout_titles.id 
        LEFT JOIN users ON workouts_timetable.trainer_id=users.id
        WHERE (`date`>='$date_from' AND `date`<= '$date_to') AND
               (free_slots>0) AND `status`='future'". "$query_part";
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
        $obj->free_slots = $row["free_slots"];
        $obj->title_id = $row["title_id"];
        $obj->workout_id = $row["workout_id"];
        $obj->trainer_id = $row["trainer_id"];
                
        $workouts[] = $obj; 
          
    }
}

echo json_encode($workouts);