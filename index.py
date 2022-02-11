import wget
import psycopg2
import subprocess
from postgis.psycopg import register

# wget dados do Paraná
url = 'http://download.openstreetmap.fr/extracts/south-america/brazil/south/parana-latest.osm.pbf'
filename = wget.download(url)
# filename = "parana-latest.osm.pbf"

dbname = "osmparana"
# estabelecendo conexão com o postgres pra criar o banco
conn = None
try:
    conn = psycopg2.connect(
    database='postgres',
    user='postgres',
    password='password',
    host='127.0.0.1',
    port='5432'
    )
    conn.autocommit = True
    with conn.cursor() as cursor:
        cursor.execute(f'CREATE DATABASE "{dbname}"')
finally:
    if conn:
        conn.close()

# conectando ao novo banco criado
conn = psycopg2.connect(
    database=dbname,
    user='postgres',
    password='password',
    host='127.0.0.1',
    port='5432'
)
conn.autocommit = True

# criando cursor
cursor = conn.cursor()

# adicionando extensões ao banco
sql = f'''
CREATE EXTENSION hstore;
CREATE EXTENSION postgis;
'''
cursor.execute(sql)
register(conn)

# usando o osm2pgsql
dbname = "osmparana"
subprocess.run(f"osm2pgsql -c -d {dbname} -U postgres {filename}", shell=True)
