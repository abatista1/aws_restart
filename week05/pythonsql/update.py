from connect import cursor as c 
import utils

db = utils.read("DB: ")
table = utils.read("Table: ")
id = utils.read("Find by ID: ")
name = utils.read("Update name: ")

try:
    sql = """UPDATE {}.dbo.{} 
        SET Name = {}
        WHERE ID = {}""".format(db,table,name,id)
    c.execute(sql)
    print(f'{id} record has been updated')
except ConnectionError:
    print("Cannot connect to SQL Server")