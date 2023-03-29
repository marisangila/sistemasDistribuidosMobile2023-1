
import xmlrpc.client as rpc
import os

client = rpc.ServerProxy('http://localhost:7000/')
client.system.listMethods()
mensagem = input("Escreva uma mensagem para ser enviada ao servidor").encode()

num1 = 5
num2 = 15

resultado = client.soma(num1,num2)
print("Soma:",resultado)

resultado = client.subtracao(num1,num2)
print("Subtração:",resultado)

resultado = client.multiplicacao(num1,num2)
print("Multiplicação:",resultado)

resultado = client.divisao(num1,num2)
print("Divisão:",resultado)

resultado = client.maior(num1,num2)
print("O numero maior e:",resultado)

client.mensagem(mensagem)
print("Mensagem")
os.system("PAUSE")