# credenciales de la bd.

import sqlite3

conexion = sqlite3.connect('usuarios.db')

cursor = conexion.cursor()

cursor.execute("SELECT * FROM users WHERE nombre = 'SANTIAGO'")
resultados = cursor.fetchall()

for registro in resultados:
    print(registro)

conexion.close()
