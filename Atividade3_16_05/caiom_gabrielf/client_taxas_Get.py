import requests
import os

#Pede ao usuário um código de área.
taxas = input("Informe o nome de um tipo de Taxa:")

#Concatena a URL e o parâmetro necessário (Nome da Taxa informado pelo usuário)
url = "https://brasilapi.com.br/api/taxas/v1/"+taxas

# Realiza a solicitação HTTP POST com os parâmetros e cabeçalhos
response = requests.get(url, headers={'Content-Type': 'application/json'})

# Verifica se a resposta foi bem sucedida (código 200)
if response.status_code == 200:

        data = response.json()

        if 'erro' not in data:  # Verifica se a API retornou um erro:
            
            # Imprime a resposta:            
            #print("Nome:", data.get('name'))
            
            print("Valor:", data.get('valor'))
            print("=======================")    
            
        else:
    # Imprime o código de erro HTTP
            print("Erro HTTP %d - %s" % (response.status_code, response.reason))           
    
os.system("PAUSE")
