import requests
import os

url = "http://127.0.0.1:5000/receber"

#payload = {'username': 'johndoe', 'password': 'secretpassword'}

# Realiza a solicitação HTTP POST com os parâmetros e cabeçalhos
response = requests.get(url, headers={'Content-Type': 'application/json'})

# Verifica se a resposta foi bem sucedida (código 200)
if response.status_code == 200:
    # Imprime o conteúdo da resposta
    print(response.json())
else:
    # Imprime o código de erro HTTP
    print("Erro HTTP %d - %s" % (response.status_code, response.reason))

os.system("PAUSE")

if __name__ == '__main__':
    app.run(debug=True)