import socket

HOST = ''  # IP do servidor
PORT = 8080  # Porta utilizada

# Cria o socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Associa o socket ao endereço e porta
s.bind((HOST, PORT))

# Aguarda uma conexão
s.listen(1)
print('Aguardando conexão...')

# Aceita a conexão
conn, addr = s.accept()
print('Conectado em', addr)

# Recebe os números do cliente
num1 = int(conn.recv(1024).decode())
num2 = int(conn.recv(1024).decode())

# Compara os números e envia uma mensagem de resposta
if num1 < num2:
    resposta = str(num1)
else:
    resposta = str(num2)
conn.sendall(resposta.encode())

# Fecha a conexão
conn.close()