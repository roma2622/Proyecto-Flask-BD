from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

#Conexion a MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_DB'] = 'escuela'
mysql = MySQL(app)

#Configuraciones
app.secret_key = 'mysecretkey'

@app.route('/')
def Index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM alumno')
    data = cur.fetchall()
    return render_template('index.html', alumnos = data)

@app.route('/agregar', methods=['POST'])
def agregar():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido1 = request.form['apellido1']
        apellido2 = request.form['apellido2']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO alumno (nombre, apellido1, apellido2) VALUES (%s, %s, %s)',
        (nombre, apellido1, apellido2))
        mysql.connection.commit()
        flash('Se ha agregado al alumno con exito')
        return redirect(url_for("Index"))

@app.route('/editar/<id>')
def get_alumno(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM alumno WHERE id = %s', (id))
    data = cur.fetchall()
    return render_template('editar_alumno.html', alumno = data[0])
    
@app.route('/update/<id>', methods = ['POST'])
def actualizar_alumno(id):
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido1 = request.form['apellido1']
        apellido2 = request.form['apellido2']
        cur = mysql.connection.cursor()
        cur.execute("""
            UPDATE alumno
            SET nombre = %s,
                apellido1 = %s,
                apellido2 = %s    
            WHERE id = %s
        """, (nombre, apellido1, apellido2, id))  
        mysql.connection.commit()
        flash('Alumno editado con exito')
        return redirect(url_for('Index'))  

@app.route('/eliminar/<string:id>')
def eliminar(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM alumno WHERE id = {0}'.format(id))
    mysql.connection.commit()
    flash('Alumno eliminado con exito')
    return redirect(url_for('Index'))
# Inicia el servidor
if __name__ == '__main__':
    app.run(port = 3000, debug = True)