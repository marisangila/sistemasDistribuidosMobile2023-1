import requests

tipoVeiculo = input("Digite o veículo:")
url = "https://brasilapi.com.br/api/fipe/marcas/v1/"+tipoVeiculo
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("Nome:", data['name'])
    print("Valor:", data['valor'])
else:
    print("Erro HTTP %d - %s" % (response.status_code, response.reason))