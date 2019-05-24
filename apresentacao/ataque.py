import random
import datetime
import urllib.parse
import socket
import requests


def primeiroDigitoCpf(lista):
    s=0
    pesos=[10,9,8,7,6,5,4,3,2]
    for i in range(len(lista)):
        s+=lista[i]*pesos[i]
    resto = s%11

    if resto==0 or resto==1:
        return 0
    else:
        return 11-resto

def segundoDigitoCpf(lista):
    s=0
    pesos=[11,10,9,8,7,6,5,4,3,2]
    for i in range(len(lista)):
        s+=lista[i]*pesos[i]
    resto=s%11

    if resto==0 or resto==1:
        return 0
    else:
        return 11-resto
def convertCpfToString(listaCpf):
    string=""
    for i in range(len(listaCpf)):
        if i==3 or i==6:
            string+="."
        if i==9:
            string+="-"
        string+=str(listaCpf[i])
    return string

def GerarCpfAleatorio():
    lista=[]
    for i in range(9):
        lista.append(random.randint(0,9))
    lista.append(primeiroDigitoCpf(lista))
    lista.append(segundoDigitoCpf(lista))

    return convertCpfToString(lista)


def GerarCelular():
    DDS=[11,12,13,14,15,16,17,18,19,21,22,24,27,28,
            31,32,33,34,35,37,38,41,42,43,44,45,46
            ,47,48,49,51,53,54,55,61,62,63,64,65,66,
            67,68,69,71,73,74,75,77,79,81,83,84,85,86
            ,87,88,89,91,93,94,95,96,97,98,99]
    string=str(DDS[random.randint(0,len(DDS)-1)])
    string+="-9"
    for i in range(8):
        if i==4:
            string+="-"
            string+=str(random.randint(0,9))

    return string

def processarNomes(listaNomes):
    for i in listaNomes:
        i= modStrip(i," ")
    


def modStrip(string,char):
    for i in range(len(string))[::-1]:
        if string[i]!=char and string[i]!="\n":
            nova=string[0:i+1]
            break
    return nova

def gerarNomes(arquivoNome):
    with open(arquivoNome,"r") as arq:
        x=arq.readlines()
    processarNomes(x)
    return x

def find_nth(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+len(needle))
        n -= 1
    return start

def gerarRandom(indice,lista):
    try:
        nome=lista[random.randint(0,len(lista))].lower()
        indice1=find_nth(nome," ",indice)
        if nome[indice1+1:indice1+3] in ["da","do","de"]:
            indice2=find_nth(nome," ",indice+2)
        else:    
            indice2=find_nth(nome," ",indice+1)
        return nome[indice1+1:indice2]
    except:
        return gerarRandom(indice,lista)

def gerarNomeCompleto(lista):
    nome=""
    x=gerarNomes("nomes.txt")
    for i in range(1,random.randint(3,7)):
            nome+=gerarRandom(i,x)+" "

    retorno=nome[:-1]
    if random.randint(1,2)%2==0:
        return retorno,retorno[:find_nth(retorno," ",retorno.count(" "))]
    else:    
        return retorno,retorno

def gerarCCA():
#cca=0000+0000+0000+0000
    string=""
    for i in range(16):
        string+=str(random.randint(0,9))
        if (i+1)%4==0:
            string+="+"
    return string[:-1]
def gerarSepa():
    string=""
    for i in range(4):
        string+=str(random.randint(0,9))
    return string
def gerarSeguranca():
    string=""
    for i in range(3):
        string+=str(random.randint(0,9))
    return string


def random_date(start, end):
    """Generate a random datetime between `start` and `end`"""
    retorno =start + datetime.timedelta(
        # Get a random amount of seconds between `start` and `end`
        seconds=random.randint(0, int((end - start).total_seconds())),
    )
    #print "retorno" , retorno
    if retorno.month >=10:
        return str(retorno.month)+"/"+str(retorno.year)
    else:
        return "0"+str(retorno.month)+"/"+str(retorno.year)



def buildReq():
    #celular=91-23892-1839&btter=continuar&cca=0000+0000+0000+0000&sepa=9999&nomeimpresso=aaaaaaaaaaaaaaaaaaaaa&validade=11%2F1111&seguranca=111&nome=aaaaaaa+aaaaaaa+aaaaaaaaaa&cpf=012.222.222-22
    #nome=andr%C3%A9+carlos+siveir%C3%A3
    #print GerarCpfAleatorio()

    #print(GerarCelular())'
    x=gerarNomes("nomes.txt")
    completo,impresso=gerarNomeCompleto(x)
    completo=urllib.parse.quote_plus(completo)
    impresso=urllib.parse.quote_plus(impresso)
    agora=datetime.datetime.now()
    depois=datetime.datetime(2030,5,17)
    
    
    post={'celular':GerarCelular(),
        'btter':'continuar',
        'cca':gerarCCA(),
        'sepa':gerarSepa(),
        'nomeimpresso':impresso,
        'validade':random_date(agora,depois),
        'seguranca':gerarSeguranca(),
        'nome':completo,
        'cpf':GerarCpfAleatorio()}
   

    return post







def main():

    padrao="""POST /final.php HTTP/1.1\r
Host: 30horasapp2019.000webhostapp.com\r
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r
Accept-Language: en-US,en;q=0.5\r
Accept-Encoding: gzip, deflate\r
Referer: http://30horasapp2019.000webhostapp.com/quarta.php\r
Content-Type: application/x-www-form-urlencoded\r
Content-Length: 190\r
Connection: close\r
Upgrade-Insecure-Requests: 1\r
\r
celular=91-23892-1839&btter=continuar&cca=0000+0000+0000+0000&sepa=9999&nomeimpresso=aaaaaaaaaaaaaaaaaaaaa&validade=11%2F1111&seguranca=111&nome=aaaaaaa+aaaaaaa+aaaaaaaaaa&cpf=012.222.222-22"""


    
    site="http://30horasapp2019.000webhostapp.com/final.php"
    payloadExample = {'celular':'91-23892-1839',
            'btter':'continuar','cca':'0000 0000 0000 0000',
            'sepa':'9999','nomeimpresso':'aaaaaaaaaaaaaaaaaaaaa',
            'validade':'11/1111','seguranca':'111','nome':'aaaaaaa aaaaaaa aaaaaaaaaa'
            ,'cpf':'012.222.222-22'}

    payload=buildReq()

    headers={
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0',
    'Referer':'http://30horasapp2019.000webhostapp.com/quarta.php'}
    # POST with form-encoded data
    
    proxy={"http":"http://127.0.0.1:8080"}

    r = requests.post(site, data=payload,headers=headers)  #,proxies=proxy)

    print("envaindo payload",payload)
    # Response, status etc
    print (r.text[1960:2005])
    print("Status",r.status_code)
    
    return     
    
    
    #cliente=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #cliente.connect((site,80))

    #cliente.send(bytes(padrao,"utf-8"))
    #resposta= cliente.recv(8000)
    #print (resposta)
    
    #request=buildReq()
    #print("testando request: ",bytes(request))

    #criamos um soquete e conectamos ele ao nosso site
    #cliente =meu_soquete_cliente(site,80)

    #pedimos para ele testar um login e uma senha na parte de login
    #enviado=cliente.testar_login("/final.php",request)

    #print("enviado",enviado)
    
    #coletamos a resposta
    #resposta=resposta_errada=cliente.receber_resposta()

    #cliente=0
    #print (resposta)



if __name__=="__main__":
    while 1:
        main()











