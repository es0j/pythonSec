<!DOCTYPE html>
<html>
<body>


<?php
if ($_POST['password']=="azgf")
{
    echo "parabéns voce acertou";
    echo "<br><img src=\"imagens/cat2.jpg\" ";
}
else
{
	echo "senha incorreta, tu ta me zoando?";
	echo "<br><img src=\"imagens/cat.jpg\" >";
	echo "postagem:".$_POST['password'];
}

?>



</body>
</html>