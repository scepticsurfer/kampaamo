<?php
$resetErr = [
    "emailErr" => "", "emailSent" => "", "emailSentErr" => "",
    "error" => ""
];
include("../navigation.php");
include("reset_password_handler.php"); 

?>

<div class="container-fluid custom-margin-for-form"> 

    <!--Row starts-->
    <div class="row">
        <div class="col-lg-2">        
        </div>

        <div class="col-lg-8">
        
            <form class="custom-form" action="" method="post">
                <h2>VAIHDA SALASANA</h2>
                <?php echo $resetErr['emailSent']; ?>
                <?php echo $resetErr['emailErr']; ?>
                <?php echo $resetErr['emailSentErr']; ?>
                <?php echo $resetErr['error']; ?>
                <div class="form-group">
                <label>Sähköposti</label>
                    <input type="email" class="form-control" name="email" id="email" />
                </div>
            
                <button type="submit" name="submit" id="submit" class="btn btn-lg btn-block custom-outline-button">Vaihda salasana
                </button>
            </form>
        
        </div>

        <div class="col-lg-2">        
        </div>
    </div>
    <!--Row ends -->

</div>

<?php
include("../footer.php");
?>