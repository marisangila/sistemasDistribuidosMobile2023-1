import requests
import os
from json import dumps

#https://jsonplaceholder.typicode.com/

url = "https://jsonplaceholder.typicode.com/comments"

continuar="1"
while continuar=="1":

    post_id = input("Digite a id do post:")
    nome_user = input("Digite o nome do usuario:")
    email_user = input("Digite o e-mail do user:")
    comentarios = input("Digite o comentario:")

    dados={"postId":post_id,
        "name":nome_user,
        "email":email_user,
        "body":comentarios}

    # Realiza a solicitação HTTP POST com os parâmetros e cabeçalhos
    response = requests.post(url, headers={'Content-Type': 'application/json'},json=dados)

    # Verifica se a resposta foi bem sucedida (código 200)
    if response.status_code == 201:
        # Imprime o conteúdo da resposta
        print(dumps(response.json(), sort_keys=True, indent=4))
        print("Dados Recebidos pela API.")
    else:
        # Imprime o código de erro HTTP
        print("Erro HTTP %d - %s" % (response.status_code, response.reason))

    continuar=input("Digite 1 para continuar ou 0 para sair:")

os.system("PAUSE")


