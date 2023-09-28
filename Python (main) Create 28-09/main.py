from flask import Flask, nombre , apellido, apellido2, curso,turno
from vinculo import conexion

def guardar(nombre, apellido1, apellido2, curso, turno):
    con = conexion()
    with con.cursor() as cursor:
        cursor.execute("INSERT INTO alumnos(nombre, apellido1, apellido2, curso, turno) VALUES (%s, %s, %s, %s, %s)",
                       (nombre, apellido1, apellido2, curso, turno))
    con.commit()
    con.close()

def mostrar():
    con = conexion()
    alumnos = []
    with con.cursor() as cursor:
        cursor.execute("SELECT id, nombre, apellido1, apellido2, turno, curso precio FROM alumnos")
    con.close()
    return alumnos

def eliminar(id)
    con = conexion()
    with con.cursor() as cursor:
        cursor.execute("DELETE FROM alumnos WHERE id = %s", (id,))
    con.commit()
    con.close()

def buscar(id):
    con = conexion()
    alumno = None
    with con.cursor() as cursor:
        cursor.execute(
            "SELECT id, nombre, apellido1, apellido2, turno, curso FROM alumnos WHERE id = %s", (id,)
        )

def actualizar(id, nombre, apellido1, apellido2, turno, curso):
    con = conexion()
    with con.cursor() as cursor:
        cursor.execute("UPDATE alumnos SET nombre = %s, apellido1 = %s, apellido2 = %s, turno = %s, curso = %s WHERE id = %s",(nombre, apellido1, apellido2, turno, curso, id))
    con.commit()
    con.close()