from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hola_mundo():
    return render_template("index.html")


@app.route('/ciclos')
def ciclos():
    return render_template("ciclos_index.html")

@app.route('/buscar/')
def buscar():
    return render_template("buscar.html")
