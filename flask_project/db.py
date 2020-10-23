import sqlite3

conn = sqlite3.connect('database.db') # Apertura y creacion de db

# Creacion de tabla en db
conn.execute('CREATE TABLE students (name TEXT, addr TEXT, city TEXT, pin TEXT)')

conn.close() # Cierra db

