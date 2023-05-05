import requests

# Este é um método GET que recebe como parâmetro um CNPJ e retorna suas informações em formato de arquivo JSON.
# Documentação: https://brasilapi.com.br/docs#tag/CNPJ
#URL: https://brasilapi.com.br/api/cnpj/v1/{cnpj}

#Solicita ao usuário um CNPJ:
cnpj = input("Digite um CNPJ:")

url = "https://brasilapi.com.br/api/cnpj/v1/"+cnpj

# Realiza a solicitação HTTP GET com os parâmetros e cabeçalhos
response = requests.get(url, headers={'Content-Type': 'application/json'})

# Verifica se a resposta foi bem sucedida (código 200)
if response.status_code == 200:
    # Imprime o conteúdo da resposta
    print(response.json())
else:
    # Imprime o código de erro HTTP
    print("Erro HTTP %d - %s" % (response.status_code, response.reason))