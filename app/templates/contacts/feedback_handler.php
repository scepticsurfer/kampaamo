<?php

   global $_emailErr,$_feefbackErr, $_feedbackSucsess;

    
    if ($_SERVER['REQUEST_METHOD'] === 'POST') {
        $name = $connect->real_escape_string(strip_tags($_POST["name"]));
        $name = filter_var($name, FILTER_SANITIZE_STRING);

        $email = $connect->real_escape_string(strip_tags($_POST["email"]));
        $email = filter_var($email, FILTER_SANITIZE_EMAIL);

        $theme = $connect->real_escape_string(strip_tags($_POST["theme"]));
        $theme = filter_var($theme, FILTER_SANITIZE_STRING);
        
        $feedback = $connect->real_escape_string(strip_tags($_POST["feedback"]));
        $feedback = filter_var($feedback, FILTER_SANITIZE_STRING);

        
        if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
            $_emailErr = '<div class="alert alert-danger">
                                Sähköpostimuoto on virheellinen.
                        </div>';
          } else{
              $feedbackQuery = "INSERT INTO feedback(date,name,email,theme,feedback) VALUE (NOW(),'$name',' $email','$theme','$feedback')";
              $result = $connect->query($feedbackQuery);
              if ($result) {
                $_feedbackSucsess = '<div class="alert alert-success" role="alert">
                                        Kiitos yhteydenotosta! Palaamme sinulle mahdollisimman pian.
                                    </div>';

                } else {
                    debuggeri("Virhe: " . $feedbackQuery . " " . $connect->error);
                    $_feefbackErr = '<div class="alert alert-danger">
                                        Virhe!
                                    </div>';
                }
        }
    }