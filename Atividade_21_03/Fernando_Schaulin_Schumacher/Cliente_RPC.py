import xmlrpc.client

def main():
    host = 'localhost'
    port = 12345

    proxy = xmlrpc.client.ServerProxy(f'http://{host}:{port}/RPC2')
    
    while True:
        operacao = input('Digite a operacao (soma, subtracao, multiplicacao, divisao, comparar) ou "sair" para encerrar: ')
        if operacao == 'sair':
            break

        valor1 = float(input('Digite o primeiro valor: '))
        valor2 = float(input('Digite o segundo valor: '))

        resultado = proxy.realizar_operacao(operacao, valor1, valor2)
        print('Resultado:', resultado)

if __name__ == '__main__':
    main()
