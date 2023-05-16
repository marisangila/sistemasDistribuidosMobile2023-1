from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

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

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

def main():
    host = 'localhost'
    port = 12345

    server = SimpleXMLRPCServer((host, port), requestHandler=RequestHandler)
    server.register_introspection_functions()
    server.register_function(realizar_operacao, 'realizar_operacao')
    print('Servidor RPC escutando na porta', port)
    server.serve_forever()

if __name__ == '__main__':
    main()
