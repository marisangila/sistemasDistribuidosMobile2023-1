import requests
import os

while True:
    # Solicita a inclusão de um CEP.
    cep = input("Informe um CEP válido para ser feito a busca:")

    # Concatena a URL e o parâmetro necessário (CEP informado pelo usuário)
    url = "https://brasilapi.com.br/api/cep/v1/"+cep

    # Realiza a solicitação HTTP GET
    response = requests.get(url)

    # Verifica se a resposta foi bem sucedida (código 200)
    if response.status_code == 200:

        data = response.json()

        if 'erro' not in data:  # Verifica se a API retornou um erro:
            
            # Imprime a resposta:
            
            print("CEP:", data.get('cep'))
            print("Estado:", data.get('state'))
            print("Cidade:", data.get('city'))
            print("Vizinhança:", data.get('neighborhood'))
            print("Rua:", data.get('street'))
            print("Serviço:", data.get('service'))
        else:
            print("CEP não encontrado.")
    else:
        # Imprime o código de erro HTTP
        print("Erro HTTP %d - %s" % (response.status_code, response.reason))
        
        break

os.system("PAUSE")