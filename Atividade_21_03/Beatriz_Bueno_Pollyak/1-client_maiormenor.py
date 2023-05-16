import socket

HOST = 'localhost'  # Endereço IP do servidor
PORT = 8080  # Porta que será utilizada

# Cria o socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conecta ao servidor
s.connect((HOST, PORT))

# Envia os números para o servidor
num1 = input("Digite o primeiro número: ")
s.sendall(num1.encode())
num2 = input("Digite o segundo número: ")
s.sendall(num2.encode())

# Recebe a mensagem de resposta do servidor
resposta = s.recv(1024).decode()
print("O menor número é", resposta)

# Fecha a conexão
s.close()4