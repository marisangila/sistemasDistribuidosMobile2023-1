from flask import Flask, request, jsonify

app = Flask(__name__)

# Lista de Livros
livros = [{
    
             'id': 1,
             'titulo': "O Senhor dos Anéis - A Sociedades do Anel",
             'autor': "J.R.R. Tolkien",
        
          },
          {
              
             'id': 2,
             'titulo': "Harry Potter e a Prdra Filosofal",
             'autor': "J.K. Howling",
        
          },
          {
              
            'id': 3,
            'titulo': "Interestelar",
            'autor': "JChristopher Nolan",
        
          },
]
# Rota para obter todos os LIVROS
@app.route('/livros', methods=['GET'])
def get_livros():
    return jsonify(livros), 200

# Rota para obter um LIVROS pelo ID
@app.route('/livros/<int:id>', methods=['GET'])
def get_livro_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro), 200
    return jsonify({'message': 'Este LIVRO não foi encontrado através desta ID'}), 404

# Rota para adicionar um novo LIVRO
@app.route('/livros', methods=['POST'])
def add_livro():
    new_livro = {
        'id': len(livros) + 1,
        'titulo': request.json['titulo'],
        'autor': request.json['autor']
    }
    livros.append(new_livro)
    return jsonify(new_livro), 201

# Rota para atualizar um LIVRO existente
@app.route('/livros/<int:livro_id>', methods=['PUT'])
def update_client(livro_id):
    for livro in livros:
        if livro['id'] == livro_id:
            livro['titulo'] = request.json['titulo']
            livro['autor'] = request.json['autor']
            return jsonify(livro), 200
    return jsonify({'message': 'Este LIVRO não foi encontrado para poder Atualizar'}), 404

# Rota para excluir um LIVRO
@app.route('/livros/<int:livro_id>', methods=['DELETE'])
def delete_livro(livro_id):
    for livro in livros:
        if livro['id'] == livro_id:
            livros.remove(livro), 200
            return jsonify({'message': 'Livro deleted'})
    return jsonify({'message': 'Este LIVRO não foi encontrado para poder Excluir'}), 404

if __name__ == '__main__':
    app.run(debug=True)