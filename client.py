import threading
import socket

def principal():

  cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  try:
    cliente.connect(('localhost', 10000))
  except:
    return print('\nnão foi possível se conectar ao servidor!\n')
  nome_cliente = input('Digite seu nome:')
  print('\nVocê esta conectado')
  print(f'\n Bem-vindo a sala de Bate-papo {nome_cliente}!\n')

  thread_1 = threading.Thread(target=receber_msg, args=[cliente])  
  thread_2 = threading.Thread(target=enviar_msg, args=[cliente, nome_cliente])


  thread_1.start()
  thread_2.start()


def receber_msg(cliente):
  while True:
    try:
      mensagem = cliente.recv(2048).decode('utf-8')
      print(mensagem + '\n')
    except:
      print('\nNão foi possível permanecer conectado\n')
      print('Presione ENTER para continuar...')
      cliente.close()
      break


def enviar_msg(cliente, nome_cliente):
  while True:
    try:
      mensagem = input('\n')
      cliente.send(f'<{nome_cliente}> {mensagem}'.encode('utf-8'))
    except:
      return

principal()