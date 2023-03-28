import xmlrpc.client as rpc
import os

client = rpc.ServerProxy('http://localhost:8080/')
client.system.listMethods()


n1 = float(input("digite um número: "))
n2 = float(input("digite um número: "))

print("Qual equação você quer fazer?")
print()
print("1 adição")
print("2 dividir")
print("3 multiplicar")
print("4 subtrair")
print()
escolher = float(input("escolha uma das opções acima: "))


if escolher == 1:
    somar = (n1)+(n2)
    print("A resultado entre",n1,"+",n2,"é",somar)

elif escolher == 2:
    dividir = (n1)/(n2)
    print("A resultado entre",n1,"÷",n2,"é",dividir)
elif escolher == 3:
    multiplicar = (n1)*(n2)
    print("A resultado entre",n1,"x",n2,"é",multiplicar)
elif escolher == 4:
    subtrair = (n1)-(n2)
    print("A resultado entre",n1,"-",n2,"é",subtrair)
else:
    print("Opção inválida,Tente novamente!")