#pip install mariadb
import mariadb
import sys

# Connect to MariaDB Platform
try:
    conn = mariadb.connect(
        user="jorge",
        password="jorge25",
        host="localhost",
        port=3306,

    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# Get Cursor
cur = conn.cursor()

#Execute SQL command
cur.execute("CREATE DATABASE Proyectobd")
cur.execute("USE Proyectobd")
cur.execute("CREATE TABLE medioPrensa(idioma VARCHAR(100),region VARCHAR(130),pais VARCHAR(100),nombre VARCHAR(100) PRIMARY KEY,url VARCHAR(2048),fechaCreacion DATE )")
cur.execute("CREATE TABLE dueño(nombre VARCHAR(100) PRIMARY KEY,personaN BOOL)")
cur.execute("CREATE TABLE administrar(fecha DATE,nombreMedio VARCHAR(100) ,nombreDueño VARCHAR(100),FOREIGN KEY (nombreMedio) REFERENCES medioPrensa(nombre),FOREIGN KEY (nombreDueño) REFERENCES dueño(nombre),PRIMARY KEY(fecha,nombreMedio,nombreDueño))")
cur.execute("CREATE TABLE noticia(idNoticia VARCHAR(100) PRIMARY KEY, url VARCHAR(2048), nombreMedio VARCHAR(100), fecha DATE, titulo VARCHAR(150), contenido TEXT, FOREIGN KEY (nombreMedio) REFERENCES medioPrensa(nombre))")
cur.execute("CREATE TABLE persona(nombre VARCHAR(100) PRIMARY KEY, fechaNacimiento DATE, profesion VARCHAR(100), nacionalidad VARCHAR(100))")
cur.execute("CREATE TABLE mencionar(idNoticia VARCHAR(100), nombrePersona VARCHAR(100), FOREIGN KEY (idNoticia) REFERENCES noticia(idNoticia), FOREIGN KEY (nombrePersona) REFERENCES persona(nombre), PRIMARY KEY(idNoticia, nombrePersona))")
cur.execute("CREATE TABLE popularidad(idPopularidad VARCHAR(100) PRIMARY KEY, fecha DATE, trafico VARCHAR(100))")
cur.execute("CREATE TABLE evaluar(nombrePersona VARCHAR(100), idPopularidad VARCHAR(100), FOREIGN KEY (nombrePersona) REFERENCES persona(nombre), FOREIGN KEY (idPopularidad) REFERENCES popularidad(idPopularidad), PRIMARY KEY(nombrePersona, idPopularidad))")

cur.execute("describe medioPrensa")
# Show results
for row in cur:
    print(row)

