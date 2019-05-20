from meu_soquete import *

cliente =meu_soquete_cliente("127.0.0.1",80)

#pegamos uma resposta errada
cliente.testar_login("/chat/login.php","login=admin&password=aaaa")
resposta_errada=cliente.receber_resposta()
print("resposta errada",resposta_errada)
