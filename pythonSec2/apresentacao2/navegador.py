from meu_soquete import *
IP="192.168.0.12"

#criamos um cliente e dizemos a qual IP queremos se conectar
cliente =meu_soquete_cliente(IP,80)

#dizemos qual paagina queremos visualizar
cliente.pedir_pagina("/chat.php?")

#mostramos a resposta na tela
print("o que foi recebido :\n",cliente.receber_resposta())
