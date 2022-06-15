#pip install mariadb
import mariadb
import sys

# Connect to MariaDB Platform
try:
    conn = mariadb.connect(
        user="jp",
        password="jp",
        host="localhost",
        port=3306,

    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# Get Cursor
cur = conn.cursor()

# Execute SQL command
#cur.execute("CREATE DATABASE Proyectobd")
cur.execute("USE Proyectobd")
#cur.execute("CREATE TABLE medioPrensa(idioma VARCHAR(100),region VARCHAR(130),pais VARCHAR(100),nombre VARCHAR(100) PRIMARY KEY,url VARCHAR(250),fechaCreacion DATE )")
#cur.execute("CREATE TABLE dueño(nombre VARCHAR(100) PRIMARY KEY,personaN BOOL)")
#cur.execute("CREATE TABLE administrar(fecha DATE,nombreMedio VARCHAR(100) ,nombreDueño VARCHAR(100),FOREIGN KEY (nombreMedio) REFERENCES medioPrensa(nombre),FOREIGN KEY (nombreDueño) REFERENCES dueño(nombre),PRIMARY KEY(fecha,nombreMedio,nombreDueño))")

cur.execute("describe medioPrensa")
# Show results
for row in cur:
    print(row)

