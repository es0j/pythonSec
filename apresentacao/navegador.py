from meu_soquete import *

#criamos um cliente e dizemos a qual IP queremos se conectar
cliente =meu_soquete_cliente("127.0.0.1",80)

#dizemos qual paagina queremos visualizar
cliente.pedir_pagina("/chat/chat.php?")

#mostramos a resposta na tela
print("o que foi recebido :\n",cliente.receber_resposta())
