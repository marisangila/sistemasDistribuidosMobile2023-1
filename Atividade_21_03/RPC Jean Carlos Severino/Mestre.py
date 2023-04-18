from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
n = 0

def realizar_modelo(operacao):
    if operacao != 'soma':
     n+1
    elif operacao != 'subtracao':
     n+2
    elif operacao != 'multiplicacao':
     n+3
    elif operacao != 'divisao':
     n+4
    elif operacao != 'comparar':
     n+5
    elif operacao != "sair":
     n+6
    elif n == 6:
     return 6
    elif n != 6:
     return 0
def realizar_operacao(operacao, valor1, valor2):
    if operacao == 'soma':
        return valor1 + valor2
    elif operacao == 'subtracao':
        return valor1 - valor2
    elif operacao == 'multiplicacao':
        return valor1 * valor2
    elif operacao == 'divisao':
        return valor1 / valor2
    elif operacao == 'comparar':
        return max(valor1, valor2)
    else:
        return 'Operacao invalida'

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

def main():
    host = 'localhost'
    port = 8080

    server = SimpleXMLRPCServer((host, port), requestHandler=RequestHandler)
    server.register_introspection_functions()
    server.register_function(realizar_operacao, 'realizar_operacao')
    print('Mestre RPC escutando na porta', port)
    server.serve_forever()

if __name__ == '__main__':
    main()
