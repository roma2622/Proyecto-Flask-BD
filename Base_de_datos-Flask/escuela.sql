DROP DATABASE IF EXISTS escuela;
CREATE DATABASE escuela CHARACTER SET utf8mb4;
USE escuela;

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

CREATE TABLE cargo (
  id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
  id_materia INT UNSIGNED NOT NULL,
  id_profesor INT UNSIGNED NOT NULL,
  id_cargo INT UNSIGNED NOT NULL,
  FOREIGN KEY (id_materia) REFERENCES materia(id),
  FOREIGN KEY (id_profesor) REFERENCES profesor(id),
  FOREIGN KEY (id_cargo) REFERENCES cargo(id)
);