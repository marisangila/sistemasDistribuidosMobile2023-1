import socket

# Lembrando que será mostrado apenas o MAIOR número.

HOST = 'localhost'  # Endereço IP do servidor
PORT = 8080  # Porta que será utilizada

# Cria o socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conecta ao servidor
s.connect((HOST, PORT))

# Envia os números para o servidor
numero_001 = input("Digite o primeiro número.......... ")
s.sendall(numero_001.encode())
numero_002 = input("Digite o segundo número........... ")
s.sendall(numero_002.encode())

# Recebe a mensagem de resposta do servidor
resposta = s.recv(1024).decode()
print("O MAIOR número é .................", resposta)

# Fecha a conexão
s.close()