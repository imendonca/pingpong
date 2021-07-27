#server.py
import socket                               # Import socket module

s = socket.socket()                         # Create a socket object
host = socket.gethostname()                 # Get local machine name
port = 12345                                # Reserve a port for your service.
s.bind((host, port))                        # Bind to the port

s.listen(5)                  
while True:               # Now wait for client connections.
    print("Esperando conexão")
    c, addr = s.accept()                     # Establish connection with client.
    print('Conectado')
    print("Esperando mensagem")
    data = ''.encode()
    while(True):
        data = c.recv(1024)
        msg = data.decode()
        if msg == 'SAIR': break

        print("Mensagem recebida: ", msg)
        info_send = input("Digite resposta: ")
        c.send(info_send.encode())
    print("Conexão encerrada")
    c.close()    