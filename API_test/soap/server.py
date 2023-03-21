from SOAPpy import Server


def mensagem(mensagem):
        return mensagem

server = Server(('localhost/mensagem',8081))
server.registerFunction(mensagem)
server.serve_forever()