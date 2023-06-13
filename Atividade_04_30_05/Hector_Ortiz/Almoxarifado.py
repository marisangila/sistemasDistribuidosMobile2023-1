from os import name
from flask import Flask, jsonify, request

app = Flask(name)

# Lista de itens no almoxarifado
itens_almoxarifado = []

# Obter todos os itens do almoxarifado
@app.route('/itens', methods=['GET'])
def get_itens_almoxarifado():
    return jsonify(itens_almoxarifado)

# Obter um item específico pelo ID
@app.route('/itens/<int:item_id>', methods=['GET'])
def get_item_almoxarifado(item_id):
    for item in itens_almoxarifado:
        if item['id'] == item_id:
            return jsonify(item), 200
    return jsonify({'message': 'Item não encontrado'}), 404

# Adicionar um novo item ao almoxarifado
@app.route('/itens', methods=['POST'])
def add_item_almoxarifado():
    novo_item = {
        'id': len(itens_almoxarifado) + 1,
        'nome': request.json['nome'],
        'quantidade': request.json['quantidade']
    }
    itens_almoxarifado.append(novo_item)
    return jsonify(novo_item), 201

# Atualizar um item do almoxarifado
@app.route('/itens/<int:item_id>', methods=['PUT'])
def update_item_almoxarifado(item_id):
    for item in itens_almoxarifado:
        if item['id'] == item_id:
            item['nome'] = request.json['nome']
            item['quantidade'] = request.json['quantidade']
            return jsonify(item), 200
    return jsonify({'message': 'Item não encontrado'}), 404

# Excluir um item do almoxarifado
@app.route('/itens/<int:item_id>', methods=['DELETE'])
def delete_item_almoxarifado(item_id):
    for item in itens_almoxarifado:
        if item['id'] == item_id:
            itens_almoxarifado.remove(item)
            return jsonify({'message': 'Item excluído'}), 200
    return jsonify({'message': 'Item não encontrado'}), 404

if name == 'main':
    app.run(debug=True)