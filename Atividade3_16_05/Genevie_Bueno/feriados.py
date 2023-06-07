import requests

ano = input("Digite o ano:")
url = "https://brasilapi.com.br/api/feriados/v1/"+ano
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
   
for feriado in data:
        print("Data:", feriado['date'])
        print("Tipo:", feriado['type'])
        print("Nome:", feriado['name'])
else:
    print("Erro HTTP %d - %s" % (response.status_code, response.reason))