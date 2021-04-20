<?php

if (isset($_POST["submit"])) {
    $password = $connect->real_escape_string(strip_tags($_POST["password"]));
    $password = filter_var($password, FILTER_SANITIZE_STRING);

    $password_2 = $connect->real_escape_string(strip_tags($_POST["password_2"]));
    $password_2 = filter_var($password_2, FILTER_SANITIZE_STRING);

    $token_password = $_POST["token_password"];

    if ($token_password != "") {
        $sqlQuery = "SELECT is_active, id FROM users LEFT JOIN users_tokens ON users.id=users_tokens.user_id WHERE token_password = '$token_password' ";
        $result = $connect->query($sqlQuery);
        $row = $result->fetch_assoc();
        $row_num = $result->num_rows;
        if ($row_num == 0) {
            $error['wrong_token'] = '<div class="alert alert-danger">
            Token on virheellinen!
         </div>';
        } else {
            $is_active = $row['is_active'];
            $user_id = $row['id'];
            if ($is_active == 0) {
                $update = "UPDATE users SET is_active = '1' WHERE id = '$user_id'";
                $result = $connect->query($update);
            }
            if (!empty($password) && !empty($password_2)) {
                if (!preg_match("/^(?=.*\d)(?=.*[@#\-_$%^&+=§!\?])(?=.*[a-z])(?=.*[A-Z])[0-9A-Za-z@#\-_$%^&+=§!\?]{6,20}$/", $password)) {
                    $error['passwordErr'] = '<div class="alert alert-danger">
                                               Salasanan tulee olla 6-20 merkkiä pituudessaan, sisältää ainakin 1 erikoismerkki, pieni kirjain, iso kirjain ja numero.
                                             </div>';
                } elseif ($password != $password_2) {
                    $error['passwords_notequal'] = '<div class="alert alert-danger">
                                               Salasanat eivät ole samanlaisia.
                                            </div>';
                } else {
                    $password_hash = password_hash($password, PASSWORD_BCRYPT);
                    $pas_Query = "UPDATE users SET password='$password_hash' WHERE id='$user_id'";
                    $result = $connect->query($pas_Query);
                    if ($result) {
                        $tok_del = "UPDATE users_tokens SET token_password=NULL WHERE token_password='$token_password'";
                        $result = $connect->query($tok_del);
                        $error['password_changed'] = '<div class="alert alert-success">
                                                                          Salasanan vaihtaminen onnistui!
                                                                       </div>';
                    } else {
                        $error['change_error'] = '<div class="alert alert-danger">
                                                                       Error!
                                                                   </div> ';
                    }
                }
            } else {

                if (empty($password)) {
                    $error['passwordEmptyErr'] = '<div class="alert alert-danger">
                                            Salasanakenttä ei voi olla tyhjä.
                                         </div>';
                }
                if (empty($password_2)) {
                    $error['password_2_EmptyErr'] = '<div class="alert alert-danger">
                                            Salasanan vahvistuskenttä ei voi olla tyhjä.
                                            </div>';
                }
            }
        }
    } else {
        $error['empty_token'] = '<div class="alert alert-danger">
                                       Token ei ole olemassa!
                                    </div>';
    }
}
