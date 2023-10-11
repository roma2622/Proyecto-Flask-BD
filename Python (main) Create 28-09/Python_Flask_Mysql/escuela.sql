-- SQLBook: Code
-- Active: 1692762019367@@127.0.0.1@3306@escuela
DROP DATABASE IF EXISTS escuela;
CREATE DATABASE escuela CHARACTER SET utf8mb4;
USE escuela;

CREATE TABLE users (
  id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(30) NOT NULL,
  password VARCHAR(50) NOT NULL
);

insert into users(nombre,password)
VALUES("root","root")



CREATE TABLE materia (
  id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(30) NOT NULL
);

CREATE TABLE profesor (
  id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(100) NOT NULL,
  apellido1 VARCHAR(100) NOT NULL,
  apellido2 VARCHAR(100)
);

CREATE TABLE curso (
  id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(50) NOT NULL,
  turno VARCHAR(30) NOT NULL
  
);

CREATE TABLE alumno (
  id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  nombre VARCHAR(100) NOT NULL,
  apellido1 VARCHAR(100) NOT NULL,
  apellido2 VARCHAR(100),
  id_curso INT UNSIGNED NOT NULL,
  FOREIGN KEY (id_curso) REFERENCES curso(id)
  
);



CREATE TABLE cargo (
  id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  id_materia INT UNSIGNED NOT NULL,
  id_profesor INT UNSIGNED NOT NULL,
  id_curso INT UNSIGNED NOT NULL,
  FOREIGN KEY (id_materia) REFERENCES materia(id),
  FOREIGN KEY (id_profesor) REFERENCES profesor(id),
  FOREIGN KEY (id_curso) REFERENCES curso(id)
);

DROP TABLE curso;

SELECT * FROM curso;

SELECT * FROM curso c inner join alumno a on c.id=a.id_curso;
INSERT INTO curso (nombre, turno) VALUES("4to2da", "Mañana");
INSERT INTO curso (nombre, turno) VALUES("4to6ta", "Vespertino");