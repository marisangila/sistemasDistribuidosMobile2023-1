import requests
import os

taxa = input("Informe a taxa:")
url = "https://brasilapi.com.br/api/taxas/v1"+taxa

response = requests.get(url, headers={'Content-Type': 'application/json'})

if response.status_code == 200:

    data = response.json()

    print("data:", data['date'])
    print("nome:", data['valor'])
    print("tipo:", data['type'])
    

else:
    # Imprime o código de erro HTTP
    print("Erro HTTP %d - %s" % (response.status_code, response.reason))
   
os.system("PAUSE")