import threading
import time

def fazerRequisicao():
    """Eu nao vou te dar o código completo. Faca o seu proprio"""
    print ('Fazendo uma requisicao pela internet...')
    time.sleep(3)
    print("acabei")
    return

threads = []
for i in range(5):
    t = threading.Thread(target=fazerRequisicao)
    threads.append(t)
    t.start()


for i in threads:
    i.join()
