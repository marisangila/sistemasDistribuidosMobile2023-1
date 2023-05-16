import requests
import json

# Definindo a URL do serviço
url = "http://localhost:8080/Add"

# Definindo os parâmetros da requisição em um dicionário Python
params = {
    "num1": 10,
    "num2": 20
}

# Convertendo o dicionário para formato JSON
json_params = json.dumps(params)

# Definindo o cabeçalho da requisição com o tipo de conteúdo esperado
headers = {"Content-Type": "application/json"}

# Enviando a requisição POST com os parâmetros JSON
response = requests.post(url, data=json_params, headers=headers)

# Verificando a resposta do servidor
if response.status_code == 200:
    result = json.loads(response.text)
    print("Resultado: ", result)
else:
    print("Erro na chamada do serviço")