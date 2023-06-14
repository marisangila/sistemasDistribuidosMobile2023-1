# Importamos as bibliotecas urllib e json
import urllib.request
import json

# Aqui estão nossas queridas moedas! Vamos junta-las em uma lista.
currencies = ['USD-BRL', 'EUR-BRL', 'BTC-BRL']

# Usamos urllib.request.urlopen para pedir as informações a API.
with urllib.request.urlopen('https://economia.awesomeapi.com.br/last/{}'.format(",".join(currencies))) as url:
    data = json.loads(url.read().decode()) # Pega o conteúdo da resposta e transforma em um objeto JSON.

# Agora, vamos percorrer a lista de moedas...
for currency in currencies:
    # A resposta da API usa um formato um pouco diferente para os códigos das moedas, então vamos ajustar nosso código de moeda para corresponder.
    api_currency_code = currency.replace('-', '')

    if api_currency_code in data: # Verifica se a moeda existe na resposta.
        # Moeda encontrada! Vamos mostrar seu nome, alta e baixa.
        print('Nome da moeda: {}'.format(data[api_currency_code]['name']))
        print('Alta do dia: {}'.format(data[api_currency_code]['high']))
        print('Baixa do dia: {}\n'.format(data[api_currency_code]['low']))
    else:
        # Parece que essa moeda não foi encontrada. Será que digitamos certo?
        print('Ah não! Não encontrei a moeda {} na API. :('.format(currency))
