import socket                          # Import socket module

s = socket.socket()                    # Create a socket object
host = socket.gethostname()            # Get local machine name
port = 12345                           # Reserve a port for your service.

print("Conectando ao servidor")
s.connect((host, port))
print("Conectado")
send_input = ''.encode()
while(True):
    send_input = input("Digite mensagem: ")
    s.send(send_input.encode())
    if (send_input == 'SAIR'): break
    print("Mensagem enviada")
    print("Esperando resposta")
    data = s.recv(1024)
    print("Resposta recebida: ", data.decode())
print("Desconectando")
s.close()    