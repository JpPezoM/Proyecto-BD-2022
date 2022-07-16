import mariadb
import sys
import spacy

nlp = spacy.load("es_core_news_md")

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

cur.execute("SELECT contenido, idNoticia FROM noticia")

# Show results
for row in cur:
    doc = nlp(row[0])
    for ent in doc.ents:
        if (ent.label_ == "PER"):
            print("Nombre: ", ent.text, "Noticia: ", row[1])