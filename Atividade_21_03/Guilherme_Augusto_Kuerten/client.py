import xmlrpc.client as rpc
import os

client = rpc.ServerProxy('http://localhost:7000/')
client.system.listMethods()
mensagem = input("digite uma mensagem para enviar ao servidor").encode()

n1 = 10
n2 = 2 

result = client.soma(n1,n2)
print("Soma:",result)

result = client.subtracao(n1,n2)
print("Subtração:",result)

result = client.multiplicacao(n1,n2)
print("Multiplicação:",result)

result = client.divisao(n1,n2)
print("Divisão:",result)

result = client.maior(n1,n2)
print("O numero maior e:",result)

client.mensagem(mensagem)
print("Mensagem")
os.system("PAUSE")