<?php
session_start();
if (!isset($_SESSION['admin']) || $_SESSION['admin']!=1) {
    die;
    }
include("../forms/db_connection.php");   
header('Content-Type: application/json');

$date_from = $connect->real_escape_string(strip_tags($_GET["date_from"]));
$date_from = filter_var($date_from, FILTER_SANITIZE_STRING);

$date_to = $connect->real_escape_string(strip_tags($_GET["date_to"]));
$date_to = filter_var($date_to, FILTER_SANITIZE_STRING);

$title_id = $connect->real_escape_string(strip_tags($_GET["title"]));
$title_id = filter_var($title_id, FILTER_SANITIZE_STRING);

$trainer_id = $connect->real_escape_string(strip_tags($_GET["trainer"]));
$trainer_id = filter_var($trainer_id, FILTER_SANITIZE_NUMBER_INT);


$query_part="";
if($trainer_id!="" && $title_id!=""){
     $query_part=" AND  ((trainer_id='$trainer_id') AND (title_id='$title_id')) ";
    }elseif($title_id!="" ){
        $query_part=" AND  title_id='$title_id' ";
    }elseif($trainer_id!=""){
        $query_part=" AND  trainer_id='$trainer_id' ";
    }


    $query = "SELECT workout_id, `date`, `time`,title,`name`,free_slots, `status` FROM workouts_timetable LEFT JOIN workout_titles
    ON workouts_timetable.title_id=workout_titles.id 
    LEFT JOIN users ON workouts_timetable.trainer_id=users.id WHERE (`date`>='$date_from' AND `date`<= '$date_to') " . "$query_part";
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
        $obj->status = $row["status"];
        $obj->workout_id = $row["workout_id"];
                        
        $workouts[] = $obj; 
          
    }
}

echo json_encode($workouts);