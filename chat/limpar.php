<?php
if ($_POST['limpar']=="123")
{
    $myfile = fopen("chat.txt", "w") or die("Unable to open file!");
    fwrite($myfile,"ola mundo!<br>");
    fclose($myfile);
}

?>