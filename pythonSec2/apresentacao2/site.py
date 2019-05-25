
#usamos o comando import quando desejamos usar
#funcoes e comandos especiais que nao estao no python
from meu_soquete import *

#uma string indica qual o conteúdo do site que deve ser mostrado
minhaPaginaWeb="""
<html>\r
<head>\r
<title>Bem vindo ao meu siteeeee</title>\r
</head>\r
<body>\r
<h1>Meu site esta rodando em python</h1>\r
<p>Este nao eh o jeito usual de criar um site, mas funciona.</p>\r
<p>Seu IP eh : %s .</p>\r
</body>\r
</html>\r
"""

#manda o servidor se conectar a uma porta
servidor =meu_soquete_servidor("0.0.0.0",8081)

#define qual pagina sera enviada 
servidor.enviar_mensagem(minhaPaginaWeb)
