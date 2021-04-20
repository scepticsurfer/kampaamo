<?php

if (!isset($_SESSION['admin']) || $_SESSION['admin']!=1) {
  die;
  }
if (isset($_POST["submit"])) {
 
  $date = $connect->real_escape_string(strip_tags($_POST["date"]));
  $date = filter_var($date, FILTER_SANITIZE_STRING);

  $time = $connect->real_escape_string(strip_tags($_POST["time"]));
  $time = filter_var($time, FILTER_SANITIZE_STRING);

  $title_id = $connect->real_escape_string(strip_tags($_POST["title"]));
  $title_id = filter_var($title_id, FILTER_SANITIZE_STRING);

  $trainer_id = $connect->real_escape_string(strip_tags($_POST["trainer"]));
  $trainer_id = filter_var((int)$trainer_id, FILTER_SANITIZE_NUMBER_INT);

  $free_slots = $connect->real_escape_string(strip_tags($_POST["free_slots"]));
  $free_slots = filter_var((int)$free_slots, FILTER_SANITIZE_NUMBER_INT);

  $status = $connect->real_escape_string(strip_tags($_POST["status"]));
  $status = filter_var($status, FILTER_SANITIZE_STRING);

  if (
    !empty($date) && !empty($time) && !empty($title_id) &&
    !empty($trainer_id) && !empty($free_slots) && !empty($status)
  ) {
    if ($date < date("Y-m-d")) {
      $error['date_error'] = '<div class="alert alert-danger">
                Päivamäärän tulee olla tänään tai sen myöhempi. 
               </div>';
    } else {
      $time_start = '08:00:00'; // sport club is opened at 08:00 AM.
      $time_finish = '21:00:00'; // sport club is closed at 22:00 and the last workout of day should be started at least an one hour before closing.
      if ($time < $time_start || $time > $time_finish) {
        $error['time_error'] = '<div class="alert alert-danger">
                Kuntoklubin aukioloajat 08:00-22:00.
                Viimeisen treenin aloitusajan tulee olla ainakin 1 tunti ennen kuntosalin sulkemista.
               </div>';
      }      
      elseif (!isset($_POST['workout_id'])) {
        $workout_check_query = "SELECT * FROM workouts_timetable 
          WHERE `date`='$date' AND time='$time' LIMIT 1";
        $result = $connect->query($workout_check_query);
        if ($result->num_rows > 0) {
          $error['workout_exist'] = '<div class="alert alert-danger">
                  Samanaikainen treeni valittuna päivänä on jo olemassa.
                 </div>';
        } else {
          $query_add = "INSERT INTO workouts_timetable(`date`, `time`, title_id,trainer_id,free_slots,`status`)
                     VALUES ('$date','$time','$title_id','$trainer_id','$free_slots','$status')";
          $result_add = $connect->query($query_add);
          if ($result_add) {
            $error['add_success'] = '<div class="alert alert-success">
                  Treenin lisääminen onnistui.
                 </div>';
          } else {
            $error['add_error'] = '<div class="alert alert-danger">
                  Jotain meni pieleen. Treenin lisääminen epäonnistui.
                 </div>';
          }
        }
      } else {
        $workout_id = $_POST['workout_id'];
        $query_change = "UPDATE  workouts_timetable SET `date`='$date', `time`='$time',
                               title_id='$title_id',trainer_id='$trainer_id',free_slots='$free_slots',`status`='$status'
                       WHERE workout_id='$workout_id'";
              
        $result_change = $connect->query($query_change);
        if ($result_change) {         
          $error['change_success'] = '<div class="alert alert-success">
                Treenin muokaaminen onnistui.
               </div>';                      
        } else {         
          $error['change_error'] = '<div class="alert alert-danger">
                Jotain meni pieleen. Treenin muokaaminen epäonnistui.                
               </div>';       
        }
      }
    }
  } else {
    $error['empty_error'] = '<div class="alert alert-danger">
    Täytä kaikki kentät.
   </div>';
  }
}