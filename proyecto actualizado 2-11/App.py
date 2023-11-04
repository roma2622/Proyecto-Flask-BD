from flask import Flask, render_template, request, redirect, url_for, flash, Response, session
from flask_mysqldb import MySQL

app = Flask(__name__)

#Conexion a MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_DB'] = 'escuela'
mysql = MySQL(app)

#Configuraciones
app.secret_key = 'mysecretkey'


#FUNCIONES ROOT 


@app.route('/agregar')
def Index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM alumno')
    data = cur.fetchall()
    return render_template('agregar.html', alumnos = data)

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
            return redirect(url_for("agregarAlumno"))
        else:
            flash('El curso no existe en la base de datos')
            return redirect(url_for("agregarAlumno"))

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

@app.route('/')
def admin():
    return render_template('login.html')   



@app.route('/admin-login', methods= ["GET", "POST"])
def login_root():
   
    if request.method == 'POST' and 'nombre' in request.form and 'password' in request.form:
       
        nombre = request.form['nombre']
        password = request.form['password']

        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM users WHERE nombre = %s AND password = %s', (nombre,password,))
        account = cur.fetchone()
      
        if account:
            session = True
            session = account

            return redirect(url_for("agregarAlumno"))
        else:
            return render_template('login.html',mensaje="Usuario o contraseña Incorrectas")


#FUNCIONES PROFESOR

@app.route('/profesor-login', methods= ["GET", "POST"])
def login_profesor():
   
    if request.method == 'POST' and 'id' in request.form and 'nombre' in request.form and 'apellido1' in request.form and 'apellido2':
       
        id=request.form['id']
        nombre = request.form['nombre']
        apellido1 = request.form['apellido1']
        apellido2 = request.form['apellido2']

        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM users WHERE id = %s , nombre = %s ,apellido1 =%s AND apellido2 = %s', (id,nombre,apellido1,apellido2,))
        account = cur.fetchone()
      
        if account:
            session = True
            session = account

            return render_template("index.html")
        else:
            return render_template('login.html',mensaje="Usuario O Contraseña Incorrectas")




#FUNCIONES ALUMNO

@app.route('/alumno-login', methods= ["GET", "POST"])
def alumno_login():
   
    if request.method == 'POST' and 'nombre' in request.form and 'password' in request.form:
       
        nombre = request.form['nombre']
        password = request.form['password']

        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM users WHERE nombre = %s AND password = %s', (nombre,password,))
        account = cur.fetchone()
      
        if account:
            session = True
            session = account

            return redirect(url_for("agregarAlumno"))
        else:
            return render_template('login.html',mensaje="Usuario o contraseña Incorrectas")





@app.route('/aconsulta-materias', methods = ["GET","POST"])
def materias_alumno(id):
    if request.method == 'POST' and 'id' in request.form:
        id = request.form['id']
        cur = mysql.connection.cursor()
        cur.execute('select m.nombre from materia m inner join alumno a on m.id=a.id where a.id =  %s')






# Inicia el servidor
if __name__ == '__main__':
    app.run(port = 3000, debug = True)

