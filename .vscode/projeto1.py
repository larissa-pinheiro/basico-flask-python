# criar um servidor local na máquina

# importa o flask
from flask import Flask, jsonify

# variável app, objeto que recebe o flask, com o name como parâmetro
app = Flask(__name__)

# o @ se chama decorator e a / irá direcionar a página para a raiz do projeto
@app.route("/")
def index():
    return "Hello World!"


# segunda página
@app.route("/rota2")
def page2():
    return "<h1>Page 2</h1>"


# quando passamos o / é somente a rota (caminho) para acessar a página, quando passamos o < > indicamos um parâmetro dentro da rota
@app.route("/pessoas/<string:nome>/string:cidade>")
def pessoa(nome, cidade):
    return jsonify({"nome": nome, "cidade": cidade})


# se eu informar os parâmetros na barra de endereço: 127.0.0.1:5000/pessoas/Maria/Rio de Janeiro
# será retornado um objeto de uma api no formato json conforme o exemplo:
# {
# "cidade": "Rio de Janeiro",
# "nome": "Maria"
# }


# inicia o servidor local e o debug=True sinaliza quando houver alguma alteração para não ter que dar stop e executar novamente
app.run(debug=True)
