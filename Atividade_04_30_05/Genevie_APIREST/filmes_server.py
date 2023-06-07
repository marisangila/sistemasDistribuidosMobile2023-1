
from flask import Flask, jsonify, request

app = Flask(__name__)

# Lista de filmes (dados simulados)
filmes = []

# Rota para obter todos os filmes
@app.route('/filmes', methods=['GET'])
def get_filmes():
    return jsonify(filmes)

# Rota para obter um filme pelo ID
@app.route('/filmes/<int:filme_id>', methods=['GET'])
def get_filme(filme_id):
    for filme in filmes:
        if filme['id'] == filme_id:
            return jsonify(filme)
    return jsonify({'message': 'filme não encontrado'}), 404

# Rota para adicionar um novo filme
@app.route('/filmes', methods=['POST'])
def add_filme():
    novo_filme = {
        'id': len(filmes) + 1,
        'nome': request.json['nome'],
        'preco': request.json['preco']
    }
    filmes.append(novo_filme)
    return jsonify(novo_filme), 201

# Rota para atualizar um filme existente
@app.route('/filmes/<int:filme_id>', methods=['PUT'])
def update_filme(filme_id):
    for filme in filmes:
        if filme['id'] == filme_id:
            filme['nome'] = request.json['nome']
            filme['preco'] = request.json['preco']
            return jsonify(filme)
    return jsonify({'message': 'filme não encontrado'}), 404

# Rota para excluir um filme
@app.route('/filmes/<int:filme_id>', methods=['DELETE'])
def delete_filme(filme_id):
    for filme in filmes:
        if filmes['id'] == filme_id:
            filmes.remove(filme)
            return jsonify({'message': 'filme excluído'})
    return jsonify({'message': 'filme não encontrado'}), 404

if __name__ == '__main__':
    app.run(debug=True)