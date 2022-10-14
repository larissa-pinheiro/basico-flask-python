from flask import Flask, render_template

app = Flask(__name__)

# o render_template importa o html especificado da pasta templates
@app.route("/")
def index():
    return render_template("index.html")


@app.route("/<string:nome>")
def error(nome):
    variavel = f"A página ({nome}) não existe."
    return render_template("error.html", variavel=variavel)


app.run(debug=True)
