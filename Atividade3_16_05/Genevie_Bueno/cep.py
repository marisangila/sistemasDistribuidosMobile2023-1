import requests

cep = input("Informe o CEP: ")

url = f"https://viacep.com.br/ws/{cep}/json/"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("Logradouro:", data['logradouro'])
    print("Bairro:", data['bairro'])
    print("Cidade:", data['localidade'])
    print("Estado:", data['uf'])
else:
    print("Erro HTTP %d - %s" % (response.status_code, response.reason))

