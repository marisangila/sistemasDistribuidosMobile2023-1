import socket

HOST = ''  # Endereço IP do servidor
PORT = 8080  # Porta que será utilizada

# Cria o socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Adiciona o socket ao endereço e porta
sock.bind((HOST, PORT))

# Aguarda uma conexão
sock.listen(1)
print('Aguardando conexão...')

# Aceita a conexão
conn, addr = sock.accept()
print('Conectado em', addr)

# Recebe a operação
operacao = conn.recv(1024).decode()

# Executa a operação e calcula o resultado
try:
    resultado = eval(operacao)
except:
    resultado = "Erro ao calcular a operação."

# Envia o resultado para o cliente
conn.sendall(str(resultado).encode())

# Fecha a conexão
conn.close()