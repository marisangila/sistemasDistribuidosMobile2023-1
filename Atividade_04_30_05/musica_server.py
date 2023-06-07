from flask import Flask, jsonify, request

app = Flask(__name__)

playlist = [
     {
         'id':1,
                'cantor': "Max Bieber",
                'nomeMusica': "Carioca Girls",
                'genero': "Pop" ,
     }
]

# Retorna a playlist inteira.
@app.route('/playlist', methods=['GET'])
def retornaPlaylist():
    return jsonify(playlist), 200

# Rota para obter uma música pelo ID (posição na playlist)
@app.route('/playlist/<int:musica_id>', methods=['GET'])
def retornaMusica(musica_id):
    for musica in playlist:
        if musica['id'] == musica_id:
            return jsonify(musica), 200
    return jsonify({'message': 'Música não encontrada!'}), 404

# Rota para adicionar uma nova música
@app.route('/musica', methods=['POST'])
def adicionaMusica():
    nova_musica = {
        'id': len(playlist) + 1,
        'cantor': request.json['cantor'],
        'genero': request.json['genero'],
        'nomeMusica': request.json['nomeMusica'],
    }
    playlist.append(nova_musica)
    return jsonify(nova_musica), 201

# Rota para atualizar uma música
@app.route('/playlist/<int:musica_id>', methods=['PUT'])
def atualizaMusica(musica_id):
    for musica in playlist:
        if musica['id'] == musica_id:
            musica['cantor'] = request.json['cantor']
            musica['nomeMusica'] = request.json['nomeMusica']
            musica['genero'] = request.json['genero']
            return jsonify(musica), 200
    return jsonify({'message': 'Música não encontrada!'}), 404

# Rota para excluir uma música
@app.route('/playlist/<int:musica_id>', methods=['DELETE'])
def deletaMusica(musica_id):
    for musica in playlist:
        if musica['id'] == musica_id:
            playlist.remove(musica)
            return jsonify({'message': 'Música deletada com sucesso!'})
    return jsonify({'message': 'Música não encontrada!'}), 404

if __name__ == '__main__':
    app.run()