<?php
// Database connection
include('./db_connection.php');

global $email_verified, $email_already_verified, $activation_error;

// GET the token = ?token
if (!empty($_GET['token'])) {
    $token = $_GET['token'];
} else {
    $token = "";
}

if ($token != "") {
    $sqlQuery = "SELECT * FROM users LEFT JOIN users_tokens ON users.id=users_tokens.user_id
                 WHERE users_tokens.token_activation = '$token'";
    $result = $connect->query($sqlQuery);

    if ($result->num_rows > 0) {
        $rowData = $result->fetch_assoc();
        $is_active = $rowData['is_active'];
        $user_id=$rowData['id'];
        if ($is_active == 0) {
            $update = "UPDATE users SET is_active = '1' WHERE id = '$user_id'";
            $result = $connect->query($update);
            if ($result) {
                $email_verified = '<div class="alert alert-success">
                                    Käyttäjän sähköpostiosoite vahvistettu!
                                </div>';
                $tok_del = "UPDATE users_tokens SET token_activation=NULL WHERE token_activation='$token'";
                $result = $connect->query($tok_del);
            }
        } else {
            $email_already_verified = '<div class="alert alert-danger">
                                        Käyttäjän sähköpostiosoite on jo vahvistettu!
                                    </div>';
        }
    } else {
        $activation_error = '<div class="alert alert-danger">
                                Aktivointivirhe!
                            </div>
                            ';
    }
}
