import socket

HOST = 'localhost'  # Endereço servidor
PORT = 8080  # Porta 

# Cria o socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conecta no servidor
sock.connect((HOST, PORT))

# Envia os números para o servidor
num1 = input("Digite o Primeiro número: ")
sock.sendall(num1.encode())
num2 = input("Digite o Segundo número: ")
sock.sendall(num2.encode())

# Recebe a mensagem de resposta
resposta = sock.recv(1024).decode()
print("Número menor", resposta)

# Fecha a conexão
sock.close()