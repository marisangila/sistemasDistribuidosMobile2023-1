import socket

HOST = ''  # IP do servidor
PORT = 8080  # Porta 

# Criação do socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Adiciona o socket ao endereço e porta
sock.bind((HOST, PORT))

# Aguarda uma conexão
sock.listen(1)
print('Aguardando conexão...')

# Aceita a conexão
conn, addr = sock.accept()
print('Conectado em', addr)

# Recebe os números do cliente
num1 = int(conn.recv(1024).decode())
num2 = int(conn.recv(1024).decode())

# Verifica os números e envia a resposta
if num1 < num2:
    resposta = str(num1)
else:
    resposta = str(num2)
conn.sendall(resposta.encode())

# Fecha a conexão
conn.close()