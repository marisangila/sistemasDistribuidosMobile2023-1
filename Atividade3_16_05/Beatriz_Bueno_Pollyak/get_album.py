import requests
import os
from json import dumps

#jsonplaceholder


foto_id=input("Digite a id do foto:")

url = "https://jsonplaceholder.typicode.com/photos/"+foto_id

# Realiza a solicitação HTTP POST com os parâmetros e cabeçalhos
response = requests.get(url, headers={'Content-Type': 'application/json'})

# Verifica se a resposta foi bem sucedida (código 200)
if response.status_code == 200:
    # Imprime o conteúdo da resposta
    print(dumps(response.json(), sort_keys=True, indent=4))
else:
    # Imprime o código de erro HTTP
    print("Erro HTTP %d - %s" % (response.status_code, response.reason))

os.system("PAUSE")

