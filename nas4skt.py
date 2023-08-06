nas4skt.py
from flask improt Flask, make_response
from markupsafe import escapefrom flask import render_template
from flask import request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('índex.html')

@app.route("/cad/usuario")
def usuario():
    return render_template("usuario.html")

@app.route("/cad/anuncio")
def anuncio():
    return render_template("anuncio.html")

@app.route("/anuncios/pergunta")
def pergunta():
    return render_template('pergunta.html')

