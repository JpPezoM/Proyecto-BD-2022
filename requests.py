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

cur.execute("USE Proyectobd;")
#¿Cuántas noticias fueron publicadas por cada medio de prensa?
cur.execute("SELECT m.nombre, count(*) FROM medioPrensa m JOIN noticia n ON m.nombre=n.nombreMedio GROUP BY n.nombreMedio ORDER BY count(*) DESC;")

#