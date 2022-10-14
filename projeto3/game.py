# o request serve para utilizar o POST e o GET

from random import randint

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    titulo = "Game: Adivinhe o número correto"

    if request.method == "GET":
        return render_template("index.html", titulo=titulo)
    else:
        numero = randint(1, 10)

        # pega o valor que a pessoa enviou no input e envia para o servidor
        palpite = int(request.form.get("name"))
        if numero == palpite:
            return "<h1>Resultado: você ganhou!</h1>"
        else:
            return "<h1>Resultado: você perdeu!</h1>"


app.run(debug=True)
