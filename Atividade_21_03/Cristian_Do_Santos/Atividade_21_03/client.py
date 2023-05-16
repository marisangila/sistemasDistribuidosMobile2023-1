import xmlrpc.client as rpc
import os

client = rpc.ServerProxy('http://localhost:8080/')
client.system.listMethods()
mensagem = input("digite uma mensagem para enviar ao servidor").encode()

a = 15
b = 10

result = client.soma(a, b);
print("Soma :", result)

result = client.subtrair(a, b);
print("subtrair :", result)

result = client.multiplicar(a, b);
print("multiplicar :", result)

result = client.dividir(a, b);
print("dividir :", result)

result = client.maiorNumero(a, b);
print("maior numero :", result)

client.mensagem(mensagem)
print("mensagem enviada")
os.system("PAUSE")