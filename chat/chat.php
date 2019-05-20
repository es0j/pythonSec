<html>
 <head>
 <title>Bem vindo ao meu chat</title>
 </head>
 <body>



<!DOCTYPE html>
<html>
<body>



 <style>
    body {
      background-color: powderblue;
    }
    h1  {
      color: blue;
    }
    p  {
      color: blue;
    }
    
    .boxed {
  border: 1px solid green ;
}
</style>


<form id="myForm2" action="?" method="post">
 <input type="hidden" name="limpar" value="0" />
 <input type="submit" value="limpar Chat" onclick="myFunction2()" />
</form>

<br> Bem vindo ao chat do ESOJ. Conversem entre si e sejam educados !</br>
<div class="boxed">
    <?php
    //Envia as respostas de uma execucao de arquivo atraves do metodos post e paramentro name
    $myfile = fopen("chat.txt", "r") or die("Unable to open file!");
    echo fread($myfile,filesize("chat.txt"));
    fclose($myfile);
    echo $_POST['name'].": ".$_POST['mensagem'];
    ?> 
</div>

<form id="myForm" action="?" method="post">
  usuario:<input name="name" value=
          <?php if ($_POST['name']!=""){
                echo $_POST['name']; 
          } 
          else{
            echo "anonimo";
          } 
          ?>
>
 mensagem: <input type="text" name="mensagem" size="50" autofocus/>
 <input type="submit" onclick="myFunction()" />
</form>




<?php
//Envia as respostas de uma execucao de arquivo atraves do metodos post e paramentro name
$myfile = fopen("chat.txt", "a") or die("Unable to open file!");
if ($_POST['mensagem']!=""){
    fwrite($myfile,$_POST['name'].": ".$_POST['mensagem']."\n<br>");
}
fclose($myfile);

if ($_POST['limpar']=="0")
{
    $myfile = fopen("chat.txt", "w") or die("Unable to open file!");
    fwrite($myfile,"ola mundo!<br>");
    fclose($myfile);
}

?>




<br> <p>Ei, eu n sou um bom programador , por favor, nao tente adivinhar minha senha de admin  <3</p><br>

<form id="myForm3" action="login.php" method="post">
<br> login:<input type="text" name="login"  />
<br> senha<input type="password" name="password"  />
  <input type="submit" value="login!" onclick="myFunction3()" />
</form>



<script>

function myFunction() {
  document.getElementById("myForm").submit();
}
function myFunctio2() {
  document.getElementById("myForm2").submit();
}
function myFunctio3() {
  document.getElementById("myForm3").submit();
}
</script>


 </body>
</html>
