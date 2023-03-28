from xmlrpc.server import SimpleXMLRPCServer


def mensagem(msg):
    print("oi")


def soma(numA, numB):
    return numA + numB


def subtracao(numA, numB):
    return numA - numB


def multiplicacao(numA, numB):
    return numA * numB


def divisao(numA, numB):
    return numA / numB


def maior(numA, numB):

    if numA >= numB:
        return numA
    else:
        return numB


server = SimpleXMLRPCServer(("localhost",8080))
print("Aguardando conexao...")
server.register_function(mensagem,'mensagem')
server.register_function(soma,'soma')
server.register_function(subtracao,'subtracao')
server.register_function(multiplicacao,'multiplicacao')
server.register_function(divisao,'divisao')
server.register_function(maior,'maior')
server.register_introspection_functions()
server.serve_forever()
