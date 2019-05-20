import socket

#exemplo de http post
"""POST /chat/login.php HTTP/1.0
Host: 127.0.0.1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Referer: http://127.0.0.1/chat/chat.php?
Content-Type: application/x-www-form-urlencoded
Content-Length: 22
Connection: close
Upgrade-Insecure-Requests: 1

login=aaa&password=aaa"""

#exemplo de get request
"""GET /chat/chat.php? HTTP/1.1\r
Host: 127.0.0.1\r
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0\r
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r
Accept-Language: pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3\r
Accept-Encoding: gzip, deflate\r
Connection: close\r
Upgrade-Insecure-Requests: 1\
Cache-Control: max-age=0\r
\r
"""
HTTP_RESPONSE="""HTTP/1.1 200 OK\r
Content-Length: %i\r
Content-type: text/html; charset=UTF-8\r
\r
%s
\r
"""

MEU_SOQUETE_HTTP_GET="""GET %s HTTP/1.0\r
Host: %s\r
\r
"""
MEU_SOQUETE_HTTP_POST="""POST %s HTTP/1.1\r
Host: %s\r
Content-Type: application/x-www-form-urlencoded\r
Content-Length: %i\r
\r
%s
\r
"""

MEU_SOQUETE_TAMANHO_MSG=10024
class meu_soquete_cliente:
    def __init__(self,endereco,porta):
        self.endereco=endereco
        self.porta=porta
        
        
        self.cliente=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.cliente.connect((endereco,porta))
        
        
    def receber_resposta(self,tamanho_resposta=2048):
        
        resp=b"1"
        resposta=b""
        while resp!=b"":
            resp=self.cliente.recv(tamanho_resposta)
            resposta+=resp
        return resposta.decode("utf-8")


    def enviar_mensagem(self,mensagem):
        #print("o que foi enviado: \n",mensagem)
        self.cliente.send(bytes(mensagem,"utf-8"))
        
        

    def pedir_pagina(self,url=""):
        return self.enviar_mensagem(
            MEU_SOQUETE_HTTP_GET%(url,self.endereco))
        
    def testar_login(self,url,formato):
        mensagem=MEU_SOQUETE_HTTP_POST%(url,self.endereco+url,len(formato),formato)
        return self.enviar_mensagem(mensagem)


    def __del__(self):
        self.cliente.close()
    #    print('Destruindo soquete.')


class meu_soquete_servidor(meu_soquete_cliente):
    def __init__(self,endereco,porta):
        self.endereco=endereco
        self.porta=porta
        self.cliente=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.cliente.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.cliente.bind((endereco,porta))
        self.cliente.listen(5)

    def enviar_mensagem(self,mensagem):

        
        while True:
            self.cliente.listen(5)
            conecao, endereco = self.cliente.accept()
            print('Connected by', endereco)

            
            mensagem_personalizada=mensagem%endereco[0]
        
                    
            
            
            
                
            data = conecao.recv(4024)
            conecao.sendall(bytes(HTTP_RESPONSE%(len(mensagem_personalizada),mensagem_personalizada),"utf-8"))
            conecao.close()
            
        
    def __del__(self):
        self.cliente.close()
    #    print('Destruindo soquete.')):




    

                    
    
if __name__=="__main__":
    #cliente =meu_soquete("www.google.com",80)
    #cliente.pedir_pagina()
    #print(cliente.receber_resposta(6000))

    #cliente =meu_soquete_cliente("127.0.0.1",80)
    #cliente.pedir_pagina("/chat/chat.php")
    #pegamos uma resposta errada
    #cliente.testar_login("/chat/login.php","login=admin&password=aaaa")
    #resposta_errada=cliente.receber_resposta()
    #print("resposta errada",resposta_errada)
    
    #brute_force()
    MSG="""<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">\r
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
    
    servidor =meu_soquete_servidor("127.0.0.1",8081)
   
    servidor.enviar_mensagem(MSG)

