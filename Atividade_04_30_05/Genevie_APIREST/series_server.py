from flask import Flask, jsonify, request

app = Flask(name)

# Lista de series (dados simulados)
series = []

# Rota para obter todos os series
@app.route('/series', methods=['GET'])
def get_series():
    return jsonify(series)

# Rota para obter uma série pelo ID
@app.route('/series/<int:serie_id>', methods=['GET'])
def get_serie(serie_id):
    for serie in series:
        if serie['id'] == serie_id:
            return jsonify(serie), 200
    return jsonify({'message': 'serie não encontrado'}), 404

# Rota para adicionar um novo serie
@app.route('/series', methods=['POST'])
def add_serie():
    novo_serie = {
        'id': len(series) + 1,
        'nome': request.json['nome'],
        'genero': request.json['genero']
    }
    series.append(novo_serie)
    return jsonify(novo_serie), 201

# Rota para atualizar um serie existente
@app.route('/series/<int:serie_id>', methods=['PUT'])
def update_serie(serie_id):
    for serie in series:
        if serie['id'] == serie_id:
            serie['nome'] = request.json['nome']
            serie['genero'] = request.json['genero']
            return jsonify(serie), 200
    return jsonify({'message': 'serie não encontrado'}), 404

# Rota para excluir um serie
@app.route('/series/<int:serie_id>', methods=['DELETE'])
def delete_serie(serie_id):
    for serie in series:
        if series['id'] == serie_id:
            series.remove(serie)
            return jsonify({'message': 'serie excluído'}), 200
    return jsonify({'message': 'serie não encontrado'}), 404

if name == 'main':
    app.run(debug=True)