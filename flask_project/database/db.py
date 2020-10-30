import sqlite3

conn = sqlite3.connect("Usuarios.db")

cursor = conn.cursor()
sql_query = """CREATE TABLE usuario (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        apellido TEXT NOT_NULL,
        correo TEXT NOT_NULL,
        tel INTEGER NOT NULL
    )"""

cursor.execute(sql_query)
