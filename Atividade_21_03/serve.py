from xmlrpc.server import SimpleXMLRPCServer

def mensagem(msg):
    print("oi")

def Soma(n1,n2):
    return n1 + n2

def Divisao(n1,n2):
    return n1 / n2

def Subtração(n1,n2):
    return n1 - n2  

def Multiplicação(n1,n2):
    return n1 * n2              

def Maior(n1,n2):
    return n1 if n1 > n2 else n2




server = SimpleXMLRPCServer(("localhost",7000))
print("Aguardando conexao...")
server.register_function(mensagem,'mensagem')
server.register_function(Soma,'Soma')
server.register_function(Divisao,'Divisão')
server.register_function(Subtração,'Subtração')
server.register_function(Multiplicação,'Multiplicação')
server.register_function(Maior,'Mario')
server.register_introspection_functions()
server.serve_forever()