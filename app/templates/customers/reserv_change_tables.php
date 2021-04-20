<?php

session_start();


if (!isset($_SESSION['loggedIn']) || $_SESSION['admin']==1 || $_SESSION['trainer']==1  ) {
    die;
    }

include("../forms/db_connection.php");

header('Content-Type: application/json');


$participant_id = $_SESSION['user_id'];

$date = $connect->real_escape_string(strip_tags($_GET['date']));
$date = filter_var($date, FILTER_SANITIZE_STRING);

$time = $connect->real_escape_string(strip_tags($_GET['time']));
$time = filter_var($time, FILTER_SANITIZE_STRING);

$title = $connect->real_escape_string(strip_tags($_GET['title']));
$title = filter_var($title, FILTER_SANITIZE_STRING);

$trainer = $connect->real_escape_string(strip_tags($_GET['trainer']));
$trainer = filter_var($trainer, FILTER_SANITIZE_STRING);


$existing = "false";
$result = "false";

$query_check = "SELECT id FROM workouts_registration WHERE participant_id='$participant_id' AND `date`='$date' AND `time`='$time'";
$result_check = $connect->query($query_check);

if ($result_check->num_rows == 0) {

    $query_serch = "SELECT workout_id,trainer_id,title_id FROM workouts_timetable WHERE `date`='$date' AND `time`='$time'";
    $result_serch = $connect->query($query_serch);
    if ($result_serch->num_rows == 0) {
        var_dump($query_insert);
        var_dump($connect->error);
    } else {
        $row = $result_serch->fetch_assoc();
        $workout_id = $row['workout_id'];
        $title_id = $row['title_id'];
        $trainer_id = $row['trainer_id'];
        $workout_id = $row['workout_id'];
       
        $connect->begin_transaction();

        $query_update = "UPDATE workouts_timetable SET free_slots=free_slots-1 WHERE workout_id='$workout_id'";
        $result_update = $connect->query($query_update);

        $query_insert = "INSERT INTO workouts_registration(`date`,`time`,workout_id,title_id,participant_id,trainer_id) 
                           VALUES ('$date','$time','$workout_id','$title_id','$participant_id','$trainer_id')";
        $result_insert = $connect->query($query_insert);
        if ($result_update && $result_insert) {
            $connect->commit();
            $result = "true";
        } else {
            $connect->rollback();
        }
    }
    
} else {
    $existing = "true";
}
$reservation = new stdClass();
$reservation->result = $result;
$reservation->existing = $existing;

echo json_encode($reservation);