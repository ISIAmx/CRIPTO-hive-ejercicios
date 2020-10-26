from flask import Flask, render_template, request, jsonify, json

app = Flask(__name__)


@app.route('/')
def hola_mundo():
    return render_template("index.html")

@app.route('/index', methods=['POST'])
def operacion():

    num1 = request.form['num1']
    print(type(num1))
    num2 = request.form['num2']
    print(type(num2))
    suma = int(num1)+int(num2)
    print(f"La suma es: {suma}")

    return json.dumps({'resultado': suma}) # Devuleve Json
