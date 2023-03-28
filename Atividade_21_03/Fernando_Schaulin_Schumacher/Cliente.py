import socket

def main():
    host = 'localhost'
    port = 12345

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))

        while True:
            operacao = input('Digite a operacao (soma, subtracao, multiplicacao, divisao, comparar) ou "sair" para encerrar: ')
            if operacao == 'sair':
                break

            valor1 = input('Digite o primeiro valor: ')
            valor2 = input('Digite o segundo valor: ')

            msg = f'{operacao} {valor1} {valor2}'
            s.sendall(msg.encode('utf-8'))
            resultado = s.recv(1024).decode('utf-8')
            print('Resultado:', resultado)

if __name__ == '__main__':
    main()
