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
for row in cur:
    doc = nlp(row[0])
    for ent in doc.ents:
        if (ent.label_ == "PER"):
            #persona mencionada
            person = ent.text
            print(person)

            #resumen wikipedia
            results= wikipedia.search(person)
            print(results)
            if (len(results) > 0):
                

                summary= wikipedia.summary(results[0], sentences=3)

                #preguntas
                result = q_a_es(question="¿En qué año nació el o ella?", context=summary)
                print("Nació en "+result["answer"])

                result = q_a_es(question="¿Cuál es su profesión?", context=summary)
                print("Su profesión es "+result["answer"])

                result = q_a_es(question="¿Cuál es su nacionalidad?", context=summary)
                print("Es "+result["answer"])

                # result=pageviewapi.per_article('es.wikipedia', person, '20200705', '20220705',
                #                 access='all-access', agent='all-agents', granularity='daily')

                # for item in result.items():
                #     for article in item[1]:
                #         views=article['views']
                #         print("Su popularidad hoy es: "+str(views)+" visitas en wikipedia español.")

                print("--------------------")
            else:
                print(person, " no ha sido encontrado en wikipedia")

            #print("Nombre: ", ent.text, "Noticia: ", row[1])