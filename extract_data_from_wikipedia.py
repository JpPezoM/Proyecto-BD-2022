import mariadb
import sys
import spacy
nlp = spacy.load("es_core_news_md")
print("spacy OK")
import wikipedia
wikipedia.set_lang("es")
import pageviewapi
print("wikipedia OK")

from transformers import AutoModelForQuestionAnswering, AutoTokenizer
from transformers import pipeline
ES_MODEL_LANGUAGE="mrm8488/bert-base-spanish-wwm-cased-finetuned-spa-squad2-es"
tokenizer_es_language = AutoTokenizer.from_pretrained(ES_MODEL_LANGUAGE)
model_es_language = AutoModelForQuestionAnswering.from_pretrained(ES_MODEL_LANGUAGE)
q_a_es = pipeline("question-answering", model=model_es_language, tokenizer=tokenizer_es_language)
print("transformers OK")

import warnings
warnings.filterwarnings("ignore")

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
print("transformers OK")
# Show results
idPopularidad = 7
cursor = cur
for row in cursor:
    doc = nlp(row[0])
    for ent in doc.ents:
        if (ent.label_ == "PER"):
            #persona mencionada
            person = ent.text
            print("Nombre: ", person, " Extraida de la noticia (id): ", row[1])

            #resumen wikipedia
            results= wikipedia.search(person)
            #print(results)
            if (len(results) > 0):
                
                try:
                    summary = wikipedia.summary(results[0], sentences = 3)
                except wikipedia.DisambiguationError as e:
                    print("No se pudo concretar la busqueda")
                    break
                #print(summary)
                #preguntas
                result = q_a_es(question="¿En qué año nació el o ella?", context=summary)
                print("Nació en "+result["answer"])
                nacimiento = result["answer"]

                result = q_a_es(question="¿Cuál es su profesión?", context=summary)
                print("Su profesión es "+result["answer"])
                profesion = result["answer"]

                result = q_a_es(question="¿Cuál es su nacionalidad?", context=summary)
                print("Es "+result["answer"])
                nacionalidad = result["answer"]

                try:
                    result=pageviewapi.per_article('es.wikipedia', person, '20210705', '20220705',
                                access='all-access', agent='all-agents', granularity='monthly')
                except pageviewapi.client.ZeroOrDataNotLoadedException as e:
                    break
                

                # query= f"INSERT INTO persona VALUES ('{person}', '{nacimiento}', '{profesion}', '{nacionalidad}');"
                # cur.execute(query)
                # conn.commit()
                # query= f"INSERT INTO mencionar VALUES ('{row[1]}', '{person}')"
                # cur.execute(query)
                # conn.commit()

                for item in result.items():
                    for article in item[1]:
                        views=article['views']
                        date=article['timestamp']
                        dateOriginal = date[0:4] + "/" + date[4:6] + "/" + date[6:8]
                        print("Su popularidad en ", dateOriginal, " es: "+str(views)+" visitas en wikipedia español.")
                        #query= f"INSERT INTO popularidad VALUES ('{idPopularidad}','{dateOriginal}' , '{str(views)}')"
                        #cur.execute(query)
                        #conn.commit()
                        #query= f"INSERT INTO evaluar VALUES ('{person}' , '{idPopularidad}')"
                        #cur.execute(query)
                        #conn.commit()
                        idPopularidad += 1



                print("--------------------")
            else:
                print("No se encontraron resultados")
                print("--------------------")
            

            #print("Nombre: ", ent.text, "Noticia: ", row[1])
#conn.close()