import requests
import os

#Pede ao usuário um código de área. 
ano = input("Informe o Ano desejado:")

#Concatena a URL e o parâmetro necessário (DDD informado pelo usuário)
url = "https://brasilapi.com.br/api/feriados/v1/"+ano

# Realiza a solicitação HTTP POST com os parâmetros e cabeçalhos
response = requests.get(url, headers={'Content-Type': 'application/json'})

# Verifica se a resposta foi bem sucedida (código 200)
if response.status_code == 200:

    data = response.json()

    for feriado in data:  
        
        #print(feriado)    
        print("Data", feriado.get('date'))        
        print("Nome", feriado.get('name'))   
        print("=======================")             
else:
    # Imprime o código de erro HTTP
    print("Erro HTTP %d - %s" % (response.status_code, response.reason))
   
os.system("PAUSE")