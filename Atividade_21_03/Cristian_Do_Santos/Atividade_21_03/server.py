from xmlrpc.server import SimpleXMLRPCServer

def mensagem(msg):
    print("oi")

def somar(n1, n2):
    return n1 + n2

def subtrair(n1, n2):
    return n1 - n2
def dividir(n1, n2):
    return n1 / n2

def mutiplicar(n1, n2):
    return n1 * n2

def maiorNumero(n1, n2):
  return n1 if n1 > n2 else n2

server = SimpleXMLRPCServer(("localhost",8080))
print("Aguardando conexao...")
server.register_function(mensagem,'mensagem')
server.register_function(somar,'somar')
server.register_function(subtrair,'subtrair')
server.register_function(dividir,'dividir')
server.register_function(mutiplicar,'mutiplicar')
server.register_function(maiorNumero,'maiorNumero')
server.register_introspection_functions()
server.serve_forever()