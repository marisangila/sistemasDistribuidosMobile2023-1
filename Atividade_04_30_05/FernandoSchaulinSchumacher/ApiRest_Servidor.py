# Aqui vamos importar algumas funções da biblioteca Flask
from flask import Flask, jsonify, request

# Este é o nosso aplicativo Flask. O __name__ é só uma convenção do Flask.
app = Flask(__name__)

# Aqui temos nosso banco de dados de veículos. Vamos começar com apenas um veículo,
# mas você pode adicionar quantos quiser. Cada veículo é um dicionário com vários atributos.
veiculos = [
    {
        'id': 1,
        'marca': "Ford",
        'cor': "Vermelho",
        'placa': "ABC-1234",
        'condutor': "José",
    }
]

# Esta é a nossa primeira rota, que retorna todos os veículos.
@app.route('/veiculos', methods=['GET'])
def retornaVeiculos():
    return jsonify(veiculos), 200  # Aqui estamos retornando os veículos em formato JSON.

# Esta rota é para obter um veículo pelo ID. Muito útil se você quiser informações sobre um veículo específico.
@app.route('/veiculos/<int:veiculo_id>', methods=['GET'])
def retornaVeiculo(veiculo_id):
    for veiculo in veiculos:
        if veiculo['id'] == veiculo_id:
            return jsonify(veiculo), 200  # Se encontrarmos o veículo, retornamos ele.
    return jsonify({'message': 'Veículo não encontrado!'}), 404  # Se não encontrarmos, retornamos uma mensagem de erro.

# Esta rota é para adicionar um novo veículo. Ela espera um JSON com os dados do veículo no corpo da requisição.
@app.route('/veiculos', methods=['POST'])
def adicionaVeiculo():
    novo_veiculo = {
        'id': len(veiculos) + 1,
        'marca': request.json['marca'],
        'cor': request.json['cor'],
        'placa': request.json['placa'],
        'condutor': request.json['condutor'],
    }
    veiculos.append(novo_veiculo)  # Adicionamos o novo veículo à nossa lista.
    return jsonify(novo_veiculo), 201  # Retornamos o novo veículo criado.

# Esta rota é para atualizar um veículo existente. Ela também espera um JSON com os novos dados do veículo.
@app.route('/veiculos/<int:veiculo_id>', methods=['PUT'])
def atualizaVeiculo(veiculo_id):
    for veiculo in veiculos:
        if veiculo['id'] == veiculo_id:
            veiculo['marca'] = request.json['marca']
            veiculo['cor'] = request.json['cor']
            veiculo['placa'] = request.json['placa']
            veiculo['condutor'] = request.json['condutor']
            return jsonify(veiculo), 200  # Se encontrarmos o veículo, atualizamos ele e o retornamos.
    return jsonify({'message': 'Veículo não encontrado!'}), 404  # Se não encontrarmos, retornamos uma mensagem de erro.

# Esta rota é para excluir um veículo. Você só precisa passar o ID do veículo na URL.
@app.route('/veiculos/<int:veiculo_id>', methods=['DELETE'])
def deletaVeiculo(veiculo_id):
    for veiculo in veiculos:
        if veiculo['id'] == veiculo_id:
            veiculos.remove(veiculo)  # Se encontrarmos o veículo, o removemos da lista.
            return jsonify({'message': 'Veículo deletado com sucesso!'}), 200
    return jsonify({'message': 'Veículo não encontrado!'}), 404  # Se não encontrarmos, retornamos uma mensagem de erro.

# Esta é a linha que inicia nosso aplicativo Flask.
if __name__ == '__main__':
    app.run()
