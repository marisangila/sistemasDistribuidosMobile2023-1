import socket

HOST = 'localhost'  # Endereço IP do servidor
PORT = 8080  # Porta que será utilizada

# Cria o socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conecta ao servidor
s.connect((HOST, PORT))

# Envia a operação para o servidor
operacao = input("Digite uma operação matemática, podendo ser uma SOMA, SUBTRAÇÃO, DIVISÃO ou MULTIPLICAÇÃO: ")
s.sendall(operacao.encode())

# Recebe o resultado da operação
resultado = s.recv(1024).decode()
print("Resultado: ", resultado)

# Fecha a conexão
# s.close()

# Para continuar com novas operações é preciso rodar (run) novamente.