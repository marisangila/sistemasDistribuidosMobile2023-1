from flask import Flask, jsonify, request

app = Flask(__name__)

# Lista de ordens de manutenção
ordens_manutencao = []

# Obter todas as ordens de manutenção
@app.route('/manutencao', methods=['GET'])
def get_ordens_manutencao():
    return jsonify(ordens_manutencao)

# Obter uma ordem de manutenção específica pelo ID
@app.route('/manutencao/<int:ordem_id>', methods=['GET'])
def get_ordem_manutencao(ordem_id):
    for ordem in ordens_manutencao:
        if ordem['id'] == ordem_id:
            return jsonify(ordem)
    return jsonify({'message': 'Ordem de manutenção não encontrada'}), 404

# Adicionar uma nova ordem de manutenção
@app.route('/manutencao', methods=['POST'])
def add_ordem_manutencao():
    nova_ordem = {
        'id': len(ordens_manutencao) + 1,
        'descricao': request.json['descricao'],
        'equipamento': request.json['equipamento']
    }
    ordens_manutencao.append(nova_ordem)
    return jsonify(nova_ordem), 201

# Atualizar informações de uma ordem de manutenção
@app.route('/manutencao/<int:ordem_id>', methods=['PUT'])
def update_ordem_manutencao(ordem_id):
    for ordem in ordens_manutencao:
        if ordem['id'] == ordem_id:
            ordem['descricao'] = request.json['descricao']
            ordem['equipamento'] = request.json['equipamento']
            return jsonify(ordem)
    return jsonify({'message': 'Ordem de manutenção não encontrada'}), 404

# Excluir uma ordem de manutenção
@app.route('/manutencao/<int:ordem_id>', methods=['DELETE'])
def delete_ordem_manutencao(ordem_id):
    for ordem in ordens_manutencao:
        if ordem['id'] == ordem_id:
            ordens_manutencao.remove(ordem)
            return jsonify({'message': 'Ordem de manutenção excluída'})
    return jsonify({'message': 'Ordem de manutenção não encontrada'}), 404

if __name__ == '__main__':
    app.run(debug=True)
