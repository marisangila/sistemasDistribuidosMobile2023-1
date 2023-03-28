# -*- coding: utf-8 -*-

import xmlrpc.client as rpc
import os

def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            break
        except ValueError:
            print("Por favor, digite um numero valido.")
    return value

client = rpc.ServerProxy('http://localhost:8080/')

message = input("Digite uma mensagem para enviar ao servidor: ").strip().encode()
response = client.handle_message(message)
print(response)

a = get_float_input("Digite o primeiro numero: ")
b = get_float_input("Digite o segundo numero: ")

try:
    print("Soma: ", client.add(a, b))
    print("Subtracao: ", client.subtract(a, b))
    print("Multiplicacao: ", client.multiply(a, b))
    print("Divisao: ", client.divide(a, b))
except rpc.Fault as e:
    print("Ocorreu um erro no servidor:", e)

os.system("PAUSE")
