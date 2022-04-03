from connect import cursor as c
from connect import connection as conn

try:
    if conn:
        print('Successfully Connected')
        c.execute("SELECT name from sys.databases")
        dbs = c.fetchall()
        print(dbs)
        c.execute("SELECT name from sys.tables")
        tables = c.fetchall()
        print(tables)
except ConnectionError:
    print("Cannot connect to SQL Server")