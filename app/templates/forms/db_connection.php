<?php
$env = parse_ini_file(__DIR__ . '/../.env');
function debuggeri($arvo)
{
    if (!defined('DEBUG') || !DEBUG) {
        return;
    }

    if (is_array($arvo) || is_object($arvo)) {
        $msg = var_export($arvo, true);
    } else {
        $msg = $arvo;
    }

    $msg = '[' . date("Y-m-d H:i:s") . "] " . $msg;
    file_put_contents("debug_log.txt", $msg . "\n", FILE_APPEND);
}

$local = in_array($_SERVER['REMOTE_ADDR'], array('127.0.0.1', '::1'));
define("DEBUG", $local);

$server = $env['server'];
$user_name = $env['user_name'];
$password = $env['password'];
$database = $env['database'];

$connect = new mysqli($server, $user_name, $password, $database);

if ($connect->connect_error) {
    debuggeri($connect->connect_error);
    echo "Yhteyden muodostaminen epäonnistui";
    die();
}

$connect->set_charset("utf8");
