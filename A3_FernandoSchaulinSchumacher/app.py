# Importando as bibliotecas necessárias para o nosso aplicativo
from flask import Flask, render_template, request, session, redirect, url_for
import pyodbc
app = Flask(__name__)
app.secret_key = '190304190304190304'  # Sua chave secreta
# Configurando a conexão com o banco de dados SQL Server
server = 'localhost'
database = 'biblioteca'
username = 'sa'
password = 'S@mu3l@2019'
driver = '{ODBC Driver 17 for SQL Server}'  # O nome do driver pode variar dependendo do driver instalado
conn_str = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}'
# Estabelecendo uma conexão persistente com o banco de dados
conn = pyodbc.connect(conn_str, autocommit=True)
# Rota inicial do aplicativo
@app.route('/')
def index():
    return 'Hello, World!'
# Rota de login. Se os dados estiverem corretos, o usuário é autenticado
# Aí, Professora Mari! Tô abrindo aqui a rota pra fazer login. Se receber um GET, vou renderizar o formulário, se for POST, vai checar as informações
@app.route('/login', methods=['GET', 'POST'])
def login():
    msg = ''
    # Checando se o método é POST e se os campos 'username' e 'password' estão presentes
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        # Capturando as informações digitadas pelo usuário
        username = request.form['username']
        password = request.form['password']

        # Criando o cursor, que vai ser tipo um intermediário entre nosso código e o banco de dados
        cursor = conn.cursor()

        # Buscando o usuário no banco com o username passado
        cursor.execute('SELECT * FROM usuarios WHERE username = ?', username)
        # Pegando o resultado da busca
        account = cursor.fetchone()

        # Se a conta existir, vamos verificar a senha
        if account:
            # Se a senha bater, vamos logar o usuário e redirecioná-lo para a rota home
            if password == account.password:
                session['loggedin'] = True
                session['id'] = account.id
                session['username'] = account.username
                return redirect(url_for("home"))
            else:
                # Senha não bateu, vamos retornar um aviso
                msg = 'Oops! A senha não está batendo. Tenta de novo?'
        else:
            # Usuário não foi encontrado, vamos retornar outro aviso
            msg = 'Hum, não estamos encontrando você. Você tem certeza que digitou o usuário certo?'
    return render_template('login.html', msg=msg)

# Aqui é a rota da página inicial. Se o usuário estiver logado, mostra a página inicial. Se não, manda pra
# página de login
@app.route('/home')
def home():
    if 'loggedin' in session:
        cursor = conn.cursor()
        cursor.execute('SELECT COUNT(*) FROM livros')
        book_count = cursor.fetchone()[0]
        return render_template('home.html', username=session['username'], book_count=book_count)
    return redirect(url_for('login'))


# Nessa rota será exibido todos os livros do banco de dados
@app.route('/read')
def read():
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM livros')
    livros = cursor.fetchall()
    return render_template('read.html', livros=livros)

# Rota para criar um novo livro. Se o método for GET, renderiza o formulário. Se for POST, insere as informações no banco de dados
@app.route('/create', methods=['GET', 'POST'])
def create():
    msg = ''
    if request.method == 'POST':
        titulo = request.form.get('titulo', '')
        escritor = request.form.get('escritor', '')
        publicadora = request.form.get('publicadora', '')
        localizacao = request.form.get('localizacao', '')

        # Se todas as informações foram preenchidas, insere no banco
        if titulo and escritor and publicadora and localizacao:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO livros (titulo, escritor, publicadora, localizacao) VALUES (?, ?, ?, ?)',
                           (titulo, escritor, publicadora, localizacao))
            msg = 'Yeah! Seu novo livro foi adicionado! Ponto Com a Professora Mari'
        else:
            # Alguma informação não foi preenchida, retorna uma mensagem de erro
            msg = 'Opa! Parece que você esqueceu de preencher algum campo.'
    return render_template('create.html', msg=msg)

# Rota para atualizar as informações de um livro
# Rota para atualizar as informações de um livro
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    cursor = conn.cursor()
    msg = ''

    if request.method == 'POST':
        titulo = request.form['titulo']
        escritor = request.form['escritor']
        publicadora = request.form['publicadora']
        localizacao = request.form['localizacao']

        # Atualiza as informações no banco
        cursor.execute('''
            UPDATE livros SET titulo = ?, escritor = ?, publicadora = ?, localizacao = ?
            WHERE id = ?
        ''', (titulo, escritor, publicadora, localizacao, id))

        msg = 'Seu livro foi atualizado com sucesso!'

    # Se o método for GET, busca as informações do livro para preencher o formulário
    cursor.execute('SELECT * FROM livros WHERE id = ?', id)
    livro = cursor.fetchone()

    return render_template('update.html', livro=livro, msg=msg)


# Rota para excluir um livro
@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    cursor = conn.cursor()
    cursor.execute('SELECT titulo FROM livros WHERE id = ?', (id,))
    livro = cursor.fetchone()
    if livro:
        livro_nome = livro[0]
        # Exclui o livro e confirma a operação
        cursor.execute('DELETE FROM livros WHERE id = ?', (id,))
        conn.commit()
        return render_template('delete.html', livro=livro_nome, msg=f'O livro "{livro_nome}" foi excluído com sucesso!')
    else:
        # Livro não foi encontrado, retorna uma mensagem de erro
        msg = 'Livro não encontrado'
        return render_template('delete.html', msg=msg)

# Rota para buscar livros
@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        search = request.form.get('bookname', '')
        cursor = conn.cursor()
        if search:
            # Procura livros com base no nome
            cursor.execute('SELECT * FROM livros WHERE titulo LIKE ?', f'%{search}%')
        else:
            # Mostra todos os livros se nenhum termo de pesquisa for fornecido
            cursor.execute('SELECT * FROM livros')
        results = cursor.fetchall()
        return render_template('search.html', results=results)
    else:
        return render_template('search.html', results=None)

# Aqui começa tudo! Vamos rodar a aplicação.
if __name__ == '__main__':
    app.run(debug=True)
