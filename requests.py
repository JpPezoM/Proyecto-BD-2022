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

cur.execute("USE Proyectobd;")
#¿Cuántas noticias fueron publicadas por cada medio de prensa?
cur.execute("SELECT m.nombre, count(*) FROM medioPrensa m JOIN noticia n ON m.nombre=n.nombreMedio GROUP BY n.nombreMedio ORDER BY count(*) DESC")
#¿Quienes son las personas mencionadas en las noticias de un día específico?
cur.execute("SELECT m.nombrePersona,n.idNoticia,n.fecha FROM noticia n JOIN mencionar m ON n.idNoticia=m.idNoticia WHERE n.fecha='2022/07/05'")
#¿Cómo evoluciona la popularidad de una persona específica?
cur.execute("SELECT p.nombre,po.fecha,po.trafico FROM persona p JOIN evaluar e ON p.nombre=e.nombrePersona JOIN popularidad po ON po.idPopularidad=e.idPopularidad WHERE p.nombre='Gabriel Boric' ORDER BY po.fecha DESC")
#¿Cuáles son los 5 medios de prensa más antiguos en una región especifica?
cur.execute("SELECT nombre, fechaCreacion FROM medioPrensa WHERE region = 'Arica y parinacota' ORDER BY fechaCreacion ASC LIMIT 5")


# Show results
for row in cur:
    print(row)