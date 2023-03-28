import xmlrpc.client as rpc
import os

client = rpc.ServerProxy('http://localhost:8080/')
client.system.listMethods()
#mensagem = input("digite uma mensagem para enviar ao servidor").encode()
#client.mensagem(mensagem)
#print("mensagem enviada")

numA = 10
numB = 2

result = client.soma(numA,numB)
print("Soma:",result)

result = client.subtracao(numA,numB)
print("Subtração:",result)

result = client.multiplicacao(numA,numB)
print("Multiplicação:",result)

result = client.divisao(numA,numB)
print("Divisão:",result)

result =  client.maior(numA,numB)
print("O número maior é:",result)




os.system("PAUSE")