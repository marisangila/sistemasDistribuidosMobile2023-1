from flask import Flask, request, jsonify

app = Flask(__name__)

#Quando esse método é chamado, ele retorna um arquivo JSON contendo a mensagem "Hello World".
@app.route("/receber", methods=["GET"])
def get():
    return jsonify([{"mensagem":"Hello World!"}]),200

#Quando esse método é chamado, ele espera receber um arquivo JSON como entrada e retorna a mensagem contida nesse arquivo.
@app.route("/enviar", methods=["POST"])
def set():
    if request.is_json:
        mensagem = request.get_json()
        return mensagem,200
    return {"error": "Request must be JSON"}, 415


if __name__ == '__main__':
    app.run(debug=True)

    #https://medium.com/python-pandemonium/build-simple-restful-api-with-python-and-flask-part-1-fae9ff66a706