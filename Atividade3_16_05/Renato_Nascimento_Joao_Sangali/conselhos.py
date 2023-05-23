import requests
import os

slip_id = input("Digite o id:")

url = "https://api.adviceslip.com/advice/"+slip_id

response = requests.get(url)

if response.status_code == 200:

    resultado = response.json()

    print (resultado['slip']['advice'])
else:
  print("Erro")
