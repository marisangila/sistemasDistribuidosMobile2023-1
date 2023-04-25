from zeep import Client

# cria um objeto cliente apontando para o arquivo WSDL do serviço
client = Client('http://localhost:8080/MyService?wsdl')

# chama o método "Add" do serviço com os parâmetros 3 e 4
result = client.service.Add(3, 4)

# imprime o resultado retornado pelo serviço
print('Resultado: ' + str(result))
