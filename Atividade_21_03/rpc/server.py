from xmlrpc.server import SimpleXMLRPCServer

def mensagem(msg):
    print(msg)

server = SimpleXMLRPCServer(("localhost",7000))
print("Aguardando conexao...")
server.register_function(mensagem,'mensagem')
server.register_introspection_functions()
server.serve_forever()
