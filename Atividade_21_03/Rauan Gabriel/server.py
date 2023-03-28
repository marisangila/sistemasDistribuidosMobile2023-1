from xmlrpc.server import SimpleXMLRPCServer

def mensagem(msg):
    print(msg)


def soma(n1,n2)
    soma = n1+n2
    return soma

def subtração(n1,n2)
    subtração = n1-n2
    return subtração

def multiplicar(n1,n2)
    multiplicar = n1*n2
    return multiplicar

def dividir(n1,n2)
    dividir = n1/n2
    return dividir

server = SimpleXMLRPCServer(("localhost",7000))
print("Aguardando conexao...")
server.register_function(mensagem,'mensagem')
server.register_introspection_functions()
server.serve_forever()