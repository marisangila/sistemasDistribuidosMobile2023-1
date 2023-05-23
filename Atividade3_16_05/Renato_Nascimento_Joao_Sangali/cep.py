import requests
import os

cep = input("Digite o cep:")

url = "https://brasilapi.com.br/api/cep/v1/"+cep

response = requests.get(url)

if response.status_code == 200:
    endereco = response.json()
    print("Estado: " + endereco.get('state'))
    print("Cidade" + endereco.get('city'))
    print("Bairro:" + endereco.get('neighborhood'))
else:
  print("Erro")
