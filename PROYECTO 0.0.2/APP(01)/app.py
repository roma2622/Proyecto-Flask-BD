from flask import Flask, redirect, render_template, request, redirect, url_for
import os #OS se utiliza para acceder a los directorios de forma mas sencilla 
import database as db

template_dir=os.path.dirname(os.path.abspath(os.path.dirname(__file__))) #esto se utiliza para poder indicar la direccion del archivo al cual acceder ("Osea el __File__")
template_dir=os.path.join(template_dir,'PROYECTO','APP')

app=Flask(__name__,template_folder=template_dir)#Esto se realizara para que el flask busque al index.html para la vinculacion.

#Rutas de la aplicacion

@app.route('/')
def home():
    cursor=db.database.cursor()
    cursor.execute("SELECT * FROM profesor")
    myresult = cursor.fetchall()
    #Convertir los datos a diccionario
    insertObject = []
    columnNames = [column[0] for column in cursor.description]
    for record in myresult: 
        insertObject.append(dict(zip(columnNames,record)))
    cursor.close
    return render_template('index.html',data=insertObject)

#Ruta para guardar usuarios en la base

@app.route('/user',methods=['POST'])
def addUser():
    nombre = request.form['nombre']
    apellido1 = request.form['apellido1']
    apellido2 = request.form['apellido2']

    if nombre and apellido1 and apellido2:
        cursor=db.database.cursor()
        sql = "INSERT INTO profesor (nombre,apellido,apellido2) VALUES (%s,%s,%s)"
        data = (nombre,apellido1,apellido2)
        cursor.execute(sql,data)
        db.database.commit()
    return redirect(url_for('home'))

@app.route('/delete/<string:id>')
def delete(id):
    cursor=db.database.cursor()
    sql="DELETE FROM profesor where id=%s"
    data=(id)
    cursor.execute(sql,data)
    db.database.commit()
    return redirect(url_for('home'))

@app.route('/edit/<string:id>',methods=['POST'])
def edit(id):
    nombre = request.form['nombre']
    apellido1 = request.form['apellido1']
    apellido2 = request.form['apellido2']

    if nombre and apellido1 and apellido2:
        cursor=db.database.cursor()
        sql = "UPDATE profesor SET nombre=%s,apellido1=%s,apellido2=%s WHERE id= %s"
        data = (nombre,apellido1,apellido2,id)
        cursor.execute(sql,data)
        db.database.commit()
    return redirect(url_for('home'))

if __name__=='__main__':
    app.run(debug=True,port=3306)