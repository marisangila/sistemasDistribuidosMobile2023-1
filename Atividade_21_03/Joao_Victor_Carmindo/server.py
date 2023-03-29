from xmlrpc.server import SimpleXMLRPCServer

def mensagem(mensagem):
    print("Hello")

def somar(num1, num2):
    return num1 + num2

def subtrair(num1, num2):
    return num1 - num2
def dividir(num1, num2):
    return num1 / num2

def mutiplicar(num1, num2):
    return num1 * num2

def maiorNumero(num1, num2):
  return num1 if num1 > num2 else num2

server = SimpleXMLRPCServer(("localhost",8080))
print("Aguardando conexão")
server.register_function(mensagem,'mensagem')
server.register_function(somar,'somar')
server.register_function(subtrair,'subtrair')
server.register_function(dividir,'dividir')
server.register_function(mutiplicar,'mutiplicar')
server.register_function(maiorNumero,'maiorNumero')
server.register_introspection_functions()
server.serve_forever()