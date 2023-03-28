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

# Recebe a operação do cliente
operacao = conn.recv(1024).decode()

# Executa a operação e calcula o resultado
try:
    resultado = eval(operacao)
except:
    resultado = "Erro ao calcular a operação."

# Envia o resultado de volta ao cliente
conn.sendall(str(resultado).encode())

# Fecha a conexão
# conn.close()