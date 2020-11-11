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


@app.route('/buscar_usuario')
def buscar_usuario():
    return render_template("buscar_usuario.html")


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


@app.route('/buscar_usuario', methods=['POST'])
def buscar_usuarios():
    opcion = ""
    json_data = request.get_json()
    if json_data['op'] == "1":
        opcion = "nombre"
        dato = json_data['nom']
    elif json_data['op'] == "2":
        opcion = "apellido"
        dato = json_data['ape']
    elif json_data['op'] == "3":
        opcion = "correo"
        dato = json_data['cor']

    print(opcion)
    print(dato)
    with conn:
        users = consultarDato(conn, opcion, dato)
        print(users)
        return (jsonify(users), 200)  # Devuleve Json


@app.route('/borrar_usuario', methods=['POST'])
def borrar_usuarios():

    json_data = request.get_json()
    id_borrar = json_data["id"]

    with conn:
        eliminarUsuario(conn, id_borrar)
        status = "Usuario Eliminado de Base de Datos"
        return json.dumps({'status': status})  # Devuleve Json


@app.route('/modificar_usuario', methods=['POST'])
def modificar_usuarios():
    
    json_data = request.get_json()

    id = json_data['id']
    nom = json_data['nom']
    apellido = json_data['ape']
    correo = json_data['cor']
    tel = json_data['tel']

    with conn:
        # Modifica Usuario
        usr = (nom, apellido, correo, tel,id)
        modificarUsuario(conn, usr)
        status = 'Modificado con éxito'
    return json.dumps({'status': status})  # Devuleve Json


if __name__ == '__main__':
    app.run(debug=True)
