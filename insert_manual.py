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

cur.execute("USE Proyectobd")
cur.execute("INSERT INTO medioPrensa VALUES ('español','Arica y parinacota','Chile','aaa','1','aaa','2012/01/28');")
cur.execute("INSERT INTO dueño VALUES ('Jose Joestar',true);")
cur.execute("INSERT INTO administrar VALUES ('2012/01/28');")
cur.execute("INSERT INTO noticia VALUES (url VARCHAR(100), nombreMedio VARCHAR(100), '2012/01/28', titulo VARCHAR(100), contenido VARCHAR(100));")
cur.execute("INSERT INTO persona VALUES ('Sebastian Piñera', '2012/01/28', 'Presidente', 'Chileno');")
cur.execute("INSERT INTO mencionar VALUES (urlNoticia VARCHAR(100), nombrePersona VARCHAR(100))")
cur.execute("INSERT INTO popularidad VALUES ('1','2012/01/28' , '20000')")
cur.execute("INSERT INTO evaluar VALUES (nombrePersona , idPopularidad)")