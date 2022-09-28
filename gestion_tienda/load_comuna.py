import sqlite3
from bs4 import BeautifulSoup
import requests
# '''function read table from wikipedia, and add comunas de Chile into table'''

response = requests.get('https://es.wikipedia.org/wiki/Anexo:Comunas_de_Chile').content
soup = BeautifulSoup(response, 'html.parser')
soup = soup.find("table").find('tbody').find_all('tr')
comunas_list = []
for communa_row in soup:
    try:
        comunas_list.append(communa_row.find('a').getText())
    except:
        pass

table = "gestion_comuna"

sqlConection = sqlite3.connect("gestion_tienda\db.sqlite3")
sqlCursor = sqlConection.cursor()


if (sqlCursor.execute(f"select count(*) from {table}").fetchone())[0] == 0:

    comunas_id = []
    for id in range(1,len(comunas_list)+1,1):
        tupla = (id, comunas_list[id-1])
        comunas_id.append(tupla)
        
    sqlCursor.executemany(f"INSERT into {table} Values(?, ?)", comunas_id)
    print("Registros Agregados")
    sqlConection.commit()

else:
    print("Warning, BD con datos, desea Eliminar [y/n]")
    res = input()
    if res == 'y':
        sqlCursor.execute(f"DELETE FROM {table}")
        sqlConection.commit()
        print("Resgistros Eliminados")

sqlConection.close()