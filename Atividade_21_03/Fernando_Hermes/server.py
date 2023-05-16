from xmlrpc.server import SimpleXMLRPCServer

def mensagem(msg):
    print(mensagem)

server = SimpleXMLRPCServer(("localhost",8080))
print("Aguardando conexao...")
server.register_function(mensagem,'mensagem')
server.register_introspection_functions()
server.serve_forever()
