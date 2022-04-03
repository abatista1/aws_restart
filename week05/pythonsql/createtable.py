from connect import cursor as c 
import utils

db = utils.read("DB: ")
table = utils.read("Create Table: ")

try:
    sql = """CREATE TABLE {}..{}(
        ID INTEGER PRIMARY KEY NOT NULL,
        Name VARCHAR(255) UNIQUE NOT NULL,
        Mark INTEGER NOT NULL,
        Grade VARCHAR(255) NOT NULL
        )""".format(db,table)
    c.execute(sql)
    print(f'{table} has been created!!!')
except ConnectionError:
    print("Cannot connect to SQL Server")