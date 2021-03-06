import mariadb
import sys
import random
from requests_html import HTMLSession
import w3lib.html
import html
import time

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

session = HTMLSession()
## URL que escrapear

listaURL=["https://www.aricamia.cl/cge-programo-mantencion-de-la-red-electrica-en-arica-para-este-lunes-18/", "https://www.aricamia.cl/proyecto-de-renovacion-de-redes-de-agua-potable-alcanza-un-100-en-su-parte-hidraulica/", "https://www.aricamia.cl/subsecretario-de-telecomunicciones-se-reune-con-autoridades-locales-para-verificar-estado-de-la-conectividad-en-la-region/", "https://www.aricamia.cl/gore-lanza-consulta-ciudadana-para-elegir-las-100-mejores-ideas-para-la-region/", "https://www.aricamia.cl/alcalde-espindola-celebra-implementacion-de-ley-de-cambio-climatico/"]

## Simular que estamos utilizando un navegador web
USER_AGENT_LIST = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
        "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
]
headers = {'user-agent':random.choice(USER_AGENT_LIST) }




## Analizar ("to parse") el contenido
xpath_title="//div//h1"
xpath_text="//div[@class='entry-content clearfix']//p"
#xpath_date="//span[@class='entry-meta-date updated']//a"



# Get Cursor
cur = conn.cursor()

cur.execute("USE Proyectobd;")

cont = 0


cur.execute("INSERT INTO medioPrensa (idioma, region, pais, nombre, url, fechaCreacion) VALUES ('espa??ol','Arica y parinacota','Chile','Arica Mia','https://www.aricamia.cl','2004/01/01')")
cur.execute("INSERT INTO due??o VALUES ('Julio Urquhart Matheu',true);")
cur.execute("INSERT INTO administrar VALUES ('2003/01/01', 'Arica Mia', 'Julio Urquhart Matheu');")

for u in listaURL:
    response = session.get(u,headers=headers)

    #Titulo de la noticia
    title = response.html.xpath(xpath_title)[0].text
    #print(title)

    #Fecha de la noticia

    #Texto de la noticia
    list_p = response.html.xpath(xpath_text)

    text=""
    for p in list_p:
            content = p.text
            content = w3lib.html.remove_tags(content)
            content = w3lib.html.replace_escape_chars(content)
            content = html.unescape(content)
            content = content.strip()
            text=text+" "+content

    #print(text)

    idNoticia = "Arica Mia " + str(cont)
    query= f"INSERT INTO noticia (idNoticia,url,nombreMedio,fecha,titulo,contenido) VALUES ('{idNoticia}', '{u}', 'Arica Mia', '2022/07/15', '{title}', '{text}')"

    cur.execute(query)
    conn.commit()
    time.sleep(1)
    cont += 1

conn.close()