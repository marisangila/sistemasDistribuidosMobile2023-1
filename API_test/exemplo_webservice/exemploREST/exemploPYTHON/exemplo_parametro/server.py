from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/Add/<int:a>/<int:b>')
def add(a, b):
    return jsonify(result=a+b)

if __name__ == '__main__':
    app.run(debug=True)
