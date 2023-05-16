import socket

# Lembrando que será mostrado apenas o MAIOR número.

HOST = ''  # Endereço IP do servidor
PORT = 8080  # Porta que será utilizada

# Cria o socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Associa o socket ao endereço e porta
s.bind((HOST, PORT))

# Aguarda uma conexão
s.listen(1)
print('Aguardando a conexão............')

# Aceita a conexão
conn, addr = s.accept()
print('Conectado em....................', addr)

# Recebe os números do cliente
numero_001 = int(conn.recv(1024).decode())
numero_002 = int(conn.recv(1024).decode())

# Compara os números e envia uma mensagem de resposta
if numero_001 > numero_002:
    resposta = str(numero_001)
else:
    resposta = str(numero_002)
conn.sendall(resposta.encode())

# Fecha a conexão
conn.close()