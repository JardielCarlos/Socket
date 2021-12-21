""" 
-----------x------------
    Autores do Código
    Jardiel / Rodrigo
-----------x------------
"""


import threading
import socket

total_clientes = []

def principal():
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        servidor.bind(('', 10000))
        servidor.listen()
        print('Aguardando conexões...')
    except:
        return print('\n Não foi possível inicar o servidor\n')
    
    while True:
        cliente, endereco = servidor.accept()
        total_clientes.append(cliente)
        print('Cliente conectado!')

        thread = threading.Thread(target=(mensagens_clientes), args=[cliente])
        thread.start()
        
def mensagens_clientes(cliente):
    while True:
        try:
            msg = cliente.recv(2048)
            broadcast(msg, cliente)
        except:
            deletar_cliente(cliente)
            break

#Broadcast manda a mensagem para todos só não envia para ele mesmo
def broadcast(mensagem, cliente):  
    for clientes in total_clientes:
        if clientes != cliente:
            try:
                clientes.send(mensagem)
            except:
                deletar_cliente(clientes)


def deletar_cliente(cliente):
    total_clientes.remove(cliente)

principal()