<?php

//if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
//die('only post');
//}
/*if (isset($_SESSION['loggedIn'])) {
  header('Location: y_tili.php');
  die();
}*/

global $wrongPwdErr, $accountNotExistErr, $namePwdErr, $verificationRequiredErr, $name_empty_err, $pass_empty_err;

if (isset($_POST['login'])) {
  $user_email = $connect->real_escape_string(stripslashes(strip_tags($_POST["user_email"])));
  $user_password = $connect->real_escape_string($_POST["user_password"]);

  if (!empty($user_email) && !empty($user_password)) {
    $pas = "SELECT * FROM users  WHERE email= '$user_email'";
    $result = $connect->query($pas);

    if ($result->num_rows > 0) {
      $row = $result->fetch_assoc();
      $user_password_base = $row['password'];
      $is_active = $row['is_active'];
      $admin = $row['admin'];
      $user_id = $row['id'];
      $trainer=$row['trainer'];

      if ($is_active == '1') {

        if (password_verify($user_password, $user_password_base)) {

          if (isset($_POST['rememberme'])) {

            setcookie("user_id", $user_id, time() + (86400 * 30), "/");
            $token_cookie = md5(rand() . time());
            $token_cookie_hash = password_hash($token_cookie, PASSWORD_DEFAULT);
            setcookie("token_cookie", $token_cookie, time() + (86400 * 30), "/");
            $expiry_date = date("Y-m-d H:i:s", time() + (86400 * 30));
            setcookie("expiry_date", $expiry_date, time() + (86400 * 30), "/");
            $hash_query = "UPDATE users_tokens SET token_cookie='$token_cookie_hash', cookie_expiry='$expiry_date' 
                            WHERE user_id='$user_id'";
            $result = $connect->query($hash_query);
          }
          $_SESSION["loggedIn"] = TRUE;
          $_SESSION['user_id'] = $user_id;
          $_SESSION['admin'] = $admin;
          $_SESSION['last_activity'] = time();
          $_SESSION['trainer']=$trainer;
          if ($admin==1) {
          header('Location: ../admins/admin_page.php');
          die();
          } elseif($trainer==1){
            header('Location: ../trainers/trainer_page.php');
            die();
           }else { 
            header('Location: ../customers/client_page.php');
            die();
           }
        } else {
          $namePwdErr = '<div class="alert alert-danger">
                              Käyttäjänimi tai salasana on virheellinen. 
                              </div>';
        }
      } else {
        $verificationRequiredErr = '<div class="alert alert-danger">
                                     Ei voi kirjautua. Tilin vahvistaminen tarvitaan.
                                    </div>';
      }
    } else {
      $accountNotExistErr = '<div class="alert alert-danger">
      Käyttäjätili ei ole olemassa. 
      </div>';
    }
  } else {
    if (empty($user_name)) {
      $name_empty_err = "<div class='alert alert-danger email_alert'>
                    Käyttäjänimi ei annettu. 
            </div>";
    }

    if (empty($user_password)) {
      $pass_empty_err = "<div class='alert alert-danger email_alert'>
                    Salasana ei annettu. 
                </div>";
    }
  }
}

$connect->close();
