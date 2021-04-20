<?php include('./user_activation.php');
$env = parse_ini_file('../.env');
?>

<!doctype html>
<html lang="en">

<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="./css/style.css">
    <title>User Verification</title>

    <!-- jQuery + Bootstrap JS -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js"></script>
</head>

<body>

    <div class="container">
        <p><br></p>
        <p><br></p>
        <div class="jumbotron text-center">
            <h1 class="display-4">SÄHKÖPOSTIOSOITTEEN VAHVISTAMINEN</h1>
            <div class="col-12 mb-5 text-center">
                <?php echo $email_already_verified; ?>
                <?php echo $email_verified; ?>
                <?php echo $activation_error; ?>
            </div>
            <p class="lead">Jos sähköpostiosoite on vahvistettu, kirjaudu sisään napsauttamalla alla olevaa painiketta.</p>
            <a class="btn btn-lg btn-danger" href="http://<?=$env['domain'] ?>/<?=$env['app_dir'] ?>/forms/login.php"
               >KIRJAUDU SISÄÄN
            </a>
        </div>
    </div>


</body>

</html>