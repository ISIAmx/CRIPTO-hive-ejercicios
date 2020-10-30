import sqlite3
from sqlite3 import Error

def conexion_db(db_file):
    # Crea conexion a db recibida por parametro
    conn = None
    try:
        conn = sqlite3.connect(db_file, check_same_thread=False)
    except Error as e:
        print(e)

    return conn  # Devuelve objeto de conexion


def insertarUsuario(conn, usr):
    # Inserta nuevo usuario
    query = f''' INSERT INTO usuario (nombre,apellido,correo,tel)
              VALUES(?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(query, usr)
    conn.commit()


def consultarUsuario(conn):
    cur = conn.cursor()

    # Obtiene todos los datos de tabla
    query = "SELECT * FROM usuario"
    cur.execute(query)

    usuarios = [
        dict(id=row[0], nombre=row[1], apellido=row[2],
             correo=row[3], tel=row[4])
        for row in cur.fetchall()
    ]
    if usuarios is not None:
        return usuarios
