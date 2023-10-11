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

#ALUMNOS
"""
    
@app.route('/')
def principal():
    cur = mysql.connection.cursor()
    return render_template('login.html')
"""

@app.route('/', methods=['POST'])
def login():
    cur = mysql.connection.cursor()
    nombre = request.form['nombre']
    password = request.form['password']
    comprobacion = cur.execute('SELECT id FROM curso WHERE nombre = %s AND password = %s', (nombre, password))
    if comprobacion == True:
        return render_template('index.html')
    else:
        flash('Usuario o Contrasena incorrectos')


@app.route('/')
def Index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM curso c inner join alumno a on c.id = a.id_curso')
    data = cur.fetchall()
    return render_template('index.html', alumnos = data)

    

@app.route('/agregar', methods=['POST'])
def agregarAlumno():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido1 = request.form['apellido1']
        apellido2 = request.form['apellido2']
        turno = request.form['turno']
        curso = request.form['curso']
        cur = mysql.connection.cursor()
        cur.execute('SELECT id FROM curso WHERE nombre = %s AND turno = %s', (curso, turno))
        curso_id = cur.fetchall()
        
        if curso_id is not None:
            # El curso existe, puedes insertar el alumno
            cur.execute('INSERT INTO alumno (nombre, apellido1, apellido2, id_curso) VALUES (%s, %s, %s, %s)',
                        (nombre, apellido1, apellido2, curso_id[0]))
            mysql.connection.commit()
            flash('Se ha agregado al alumno con éxito')
            return redirect(url_for("Index"))
        else:
            flash('El curso no existe en la base de datos')
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
def eliminarAlumno(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM alumno WHERE id = {0}'.format(id))
    mysql.connection.commit()
    flash('Alumno eliminado con exito')
    return redirect(url_for('Index'))

#PROFESORES
"""
@app.route('/agregar', methods=['POST'])
def agregarProfesor():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido1 = request.form['apellido1']
        apellido2 = request.form['apellido2']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO profesor (nombre, apellido1, apellido2) VALUES (%s, %s, %s)',
        (nombre, apellido1, apellido2))
        mysql.connection.commit()
        flash('Se ha agregado al profesor con exito')
        return redirect(url_for("Index"))

@app.route('/editar/<id>')
def get_profesor(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM profesor WHERE id = %s', (id))
    data = cur.fetchall()
    return render_template('editar_profesor.html', profesor = data[0])
"""
"""
@app.route('/update/<id>', methods = ['POST'])
def actualizar_profesor(id):
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido1 = request.form['apellido1']
        apellido2 = request.form['apellido2']
        cur = mysql.connection.cursor()
 #       cur.execute("""

#            UPDATE profesor
 #           SET nombre = %s,
  #              apellido1 = %s,
   #             apellido2 = %s    
    #        WHERE id = %s
       # """, (nombre, apellido1, apellido2, id))  
"""
        mysql.connection.commit()
        flash('profesor editado con exito')
        return redirect(url_for('Index'))  

@app.route('/eliminar/<string:id>')
def eliminarProfesor(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM profesor WHERE id = {0}'.format(id))
    mysql.connection.commit()
    flash('profesor eliminado con exito')
    return redirect(url_for('Index'))
"""








#FUNCIONES DE INICIO DE SESION (CREO QUE NO FUNCIONAN ASI QUE VOY A VER ESTE VIDEO)
#https://www.youtube.com/watch?v=FX0lMm_Qj10

"""
@app.route('/')
def login():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM curso c inner join a alumno on c.id = a.id_curso')
    data = cur.fetchall()
    return render_template('login.html', alumnos = data)

@app.route('/verificar', methods =['POST'])
def inicio_root():
    if request.method == 'POST':
        nombre = request.form['nombre']
        password = request.form['password']
    cur = mysql.connection.cursor()
    cur.execute('SELECT nombre,password FROM user WHERE nombre = %s and password = %s')
 
 

 



"""








# Inicia el servidor
if __name__ == '__main__':
    app.run(port = 3000, debug = True)