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

