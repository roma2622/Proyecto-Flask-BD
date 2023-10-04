from flask import Flask, render_template
import os #OS se utiliza para acceder a los directorios de forma mas sencilla 
import conexion as con

template_dir=os.path.dirname(os.path.abspath(os.path.dirname(__file__))) #esto se utiliza para poder indicar la direccion del archivo al cual acceder ("Osea el __File__")
template_dir=os.path.join(template_dir,'PROYECTO','APP')

app=Flask(__name__,template_folder=template_dir)#Esto se realizara para que el flask busque al index.html para la vinculacion.

#Rutas de la aplicacion

app.route('/')
def home():

    return render_template('index.html')


if __name__=='__main__':
    app.run(debug=True,port=5500)