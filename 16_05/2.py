import requests
import os

# Calcula os feriados

ano = input("Digite o ano:")

url = "https://brasilapi.com.br/api/feriados/v1/{ano}" + ano

response = requests.get(url, headers={'Content-Type': 'application/json'})

if response.status_code == 200:

    data = response.json()

    print("data:", data['date'])
    print("nome:", data['name'])
    print("tipo:", data['type'])

    
   
else:
    print("Erro HTTP %d - %s" % (response.status_code, response.reason))
   
os.system("PAUSE")