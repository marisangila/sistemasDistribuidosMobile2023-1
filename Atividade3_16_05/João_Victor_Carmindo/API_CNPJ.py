import requests
import os

cnpj = input("Informe o cnpj:")
url = "https://brasilapi.com.br/api/cnpj/v1/"+cnpj


response = requests.get(url, headers={'Content-Type': 'application/json'})


if response.status_code == 200:

    data = response.json()

    print("Nome:", data['razao_social'])
    print("Descrição:", data['cnae_fiscal_descricao'])
    print("Data de inicio:", data['data_inicio_atividade'])
    print("Logradouro:", data['logradouro'])
    
   
else:
   
    print("Erro HTTP %d - %s" % (response.status_code, response.reason))
   
os.system("PAUSE")