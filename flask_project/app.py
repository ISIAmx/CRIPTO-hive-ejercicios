from flask import Flask, render_template, request, json, jsonify
import sqlite3
from database.db_conf import *


app = Flask(__name__)
database = r"database/Usuarios.db"

# Crea conexion a db
conn = conexion_db(database)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/users')
def users():
    return render_template("users.html")


@app.route('/index', methods=['POST'])
def operacion():
    json_data = request.get_json()

    nom = json_data['nom']
    apellido = json_data['ape']
    correo = json_data['cor']
    tel = json_data['tel']

    with conn:
        # Inserta Usuario
        usr = (nom, apellido, correo, tel)
        insertarUsuario(conn, usr)
        status = 'Registrado con éxito'
    return json.dumps({'status': status})  # Devuleve Json


@app.route('/users', methods=['POST'])
def ver_usuarios():
    json_data = request.get_json()

    btn = json_data['click']
  
    if btn == 'true':
        with conn:
            users = consultarUsuario(conn)
            return (jsonify(users), 200)  # Devuleve Json


if __name__ == '__main__':
    app.run(debug=True)
