import socket

def realizar_operacao(tipo, valor1, valor2):
    if tipo == 'soma':
        return valor1 + valor2
    elif tipo == 'subtracao':
        return valor1 - valor2
    elif tipo == 'multiplicacao':
        return valor1 * valor2
    elif tipo == 'divisao':
        return valor1 / valor2
    elif tipo == 'comparar':
        return max(valor1, valor2)
    else:
        return 'Operacao invalida'

def main():
    host = 'localhost'
    port = 12345

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print('Servidor escutando na porta', port)

        conn, addr = s.accept()
        with conn:
            print('Conectado por', addr)
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                
                operacao, valor1, valor2 = data.decode('utf-8').split()
                resultado = realizar_operacao(operacao, float(valor1), float(valor2))
                conn.sendall(str(resultado).encode('utf-8'))

if __name__ == '__main__':
    main()


