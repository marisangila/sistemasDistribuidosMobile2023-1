import requests
import os

url = "http://127.0.0.1:5000/enviar"

mensagem = {'mensagem': "Hello World!"}

# Realiza a solicitação HTTP POST com os parâmetros e cabeçalhos
response = requests.post(url, headers={'Content-Type': 'application/json'},json=mensagem)

# Verifica se a resposta foi bem sucedida (código 200)
if response.status_code == 200:
    # Imprime o conteúdo da resposta
    print(response.json())
    print("Dados Recebidos pela API.")
else:
    # Imprime o código de erro HTTP
    print("Erro HTTP %d - %s" % (response.status_code, response.reason))

os.system("PAUSE")


