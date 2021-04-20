<?php

session_start();
if (!isset($_SESSION['loggedIn']) || $_SESSION['admin']==1 || $_SESSION['trainer']==1  ) {
    die;
    }

include("../forms/db_connection.php");

header('Content-Type: application/json');

$result = "false";

$participant_id = $_SESSION['user_id'];

$date = $connect->real_escape_string(strip_tags($_GET['date']));
$date = filter_var($date, FILTER_SANITIZE_STRING);

$time = $connect->real_escape_string(strip_tags($_GET['time']));
$time = filter_var($time, FILTER_SANITIZE_STRING);

$query_serch = "SELECT workout_id FROM workouts_timetable WHERE `date`='$date' AND `time`='$time'";
$result_serch = $connect->query($query_serch);
if ($result_serch->num_rows == 0) {
    var_dump($query_search);
    var_dump($connect->error);
} else {
    $row = $result_serch->fetch_assoc();
    $workout_id = $row['workout_id'];

    $query_update = "UPDATE workouts_timetable SET free_slots=free_slots+1 WHERE workout_id='$workout_id'";
    $result_update = $connect->query($query_update);

    $query_delete = "DELETE FROM workouts_registration WHERE `date`='$date' AND `time`='$time' AND participant_id='$participant_id'";
    $result_delete = $connect->query($query_delete);

    
    if ($result_update && $result_delete) {
        $connect->commit();
        $result = "true";
    } else {
        $connect->rollback();
    }
}

echo json_encode($result);