#pip install mariadb
import mariadb
import sys

# Connect to MariaDB Platform
try:
    conn = mariadb.connect(
        user="jp",
        password="kititi123",
        host="localhost",
        port=3306,

    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# Get Cursor
cur = conn.cursor()

cur.execute("USE Proyectobd")
cur.execute("INSERT INTO medioPrensa (idioma, region, pais, nombre, url, fechaCreacion) VALUES ('español','Arica y parinacota','Chile','El Morrocotudo','https://www.elmorrocotudo.cl','2005/01/01')")
cur.execute("INSERT INTO dueño VALUES ('GrupoMiVoz',false);")
cur.execute("INSERT INTO administrar VALUES ('2005/01/01', 'El Morrocotudo', 'GrupoMiVoz');")
cur.execute("INSERT INTO noticia VALUES ('0', 'https://www.elmorrocotudo.cl/noticia/economia/repoblamiento-de-sectores-rurales-seremi-de-transportes-de-arica-redisenara-transpo', 'El Morrocotudo', '2022/07/05', 'Repoblamiento de Sectores Rurales: Seremi de Transportes de Arica rediseñará transporte rural', ' Cuando se realizó el CENSO del 2017 la población de la Región alcanzó a las 226.068 personas. De ese total el 97,9% de ellos declaró vivir en la comuna de Arica, 1,2% en la comuna de Putre, 0,6% en la comuna de Camarones y 0,3% en la comuna de General Lagos. ');")
cur.execute("INSERT INTO persona VALUES ('Pablo Maturana', '1992/01/28', 'Seremi de transportes', 'Chileno');")
cur.execute("INSERT INTO persona VALUES ('Gabriel Boric', '1992/01/28', 'Presidente', 'Chileno');")
cur.execute("INSERT INTO mencionar VALUES ('0', 'Pablo Maturana')")
cur.execute("INSERT INTO mencionar VALUES ('0', 'Gabriel Boric')")
cur.execute("INSERT INTO popularidad VALUES ('0','2022/07/06' , '0')")
cur.execute("INSERT INTO evaluar VALUES ('Pablo Maturana' , '0')")
cur.execute("commit;")
conn.close()