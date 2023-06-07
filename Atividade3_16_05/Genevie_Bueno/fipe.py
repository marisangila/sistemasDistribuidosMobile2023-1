import requests

codigoFipe = input("Digite o código Fipe:")
url = "https://brasilapi.com.br/api/fipe/preco/v1/"+codigoFipe
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("Valor:", data['valor'])
    print("Marca:", data['marca'])
    print("Modelo:", data['modelo'])
    print("Ano:", data['anoModelo'])
    print("Combustivel:", data['combustivel'])
    print("Código data:", data['codigoFipe'])
    print("Mês Referência:", data['mesReferencia'])
    print("Tipo de Veiculo:", data['tipoVeiculo'])
    print("Sigla Combustivel:", data['siglaCombustivel'])
    print("Data da Consulta:", data['dataConsulta'])
else:
    print("Erro HTTP %d - %s" % (response.status_code, response.reason))

