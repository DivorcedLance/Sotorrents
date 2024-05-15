from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Ruta de la página principal
@app.route('/')
def index():
    return '¡Hola, mundo!'

# Ruta para mostrar los datos de la base de datos
@app.route('/datos')
def mostrar_datos():
    # Conexión a la base de datos
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Consulta para obtener los datos de la tabla
    cursor.execute('SELECT * FROM tabla')
    datos = cursor.fetchall()

    # Cerrar la conexión a la base de datos
    cursor.close()
    conn.close()

    return render_template('datos.html', datos=datos)

if __name__ == '__main__':
    app.run(debug=True)