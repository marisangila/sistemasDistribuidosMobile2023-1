import socket

HOST = ''  # Endereço IP do servidor
PORT = 1024  # Porta que será utilizada

# Cria o socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conecta ao servidor
s.connect((HOST,PORT))

# Envia a operação para o servidor
operacao = input("Digite a operação matemática a ser realizada: ")
s.sendall(operacao.encode())

# Recebe o resultado da operação
resultado = s.recv(1024).decode()
print("Resultado: ", resultado)

# Fecha a conexão
# s.close()