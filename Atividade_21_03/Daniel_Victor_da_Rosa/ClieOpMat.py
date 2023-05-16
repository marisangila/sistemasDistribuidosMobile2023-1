import socket

HOST = 'localhost'  # IP do servidor
PORT = 8080  # Porta 

# Cria o socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conecta ao servidor
sock.connect((HOST, PORT))

# Envia a operação para o servidor
operacao = input("Digite a operação matemática a ser realizada: ")
sock.sendall(operacao.encode())

# Recebe o resultado 
resultado = sock.recv(1024).decode()
print("Resultado: ", resultado)

# Fecha a conexão
sock.close()