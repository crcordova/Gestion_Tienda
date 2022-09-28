import sqlite3
from bs4 import BeautifulSoup
import requests

url = 'https://regionesdechile.cl/'

response = requests.get(url).content
soup = BeautifulSoup(response, 'html.parser')
soup = soup.find("tbody").find_all('a')
regions_list = []
for region in soup:
    try:
        regions_list.append((region.getText(),))
    except:
        pass

print(regions_list)
table = "gestion_region"

sqlConection = sqlite3.connect("gestion_tienda\db.sqlite3")
sqlCursor = sqlConection.cursor()

if (sqlCursor.execute(f"select count(*) from {table}").fetchone())[0] == 0:
    sqlCursor.executemany(f"INSERT into {table} Values(?)", regions_list)
    sqlConection.commit()
    print("Regiones Agregadas a la BD")
else:
    print("error al insertar, ya existen datos")

sqlConection.close()