import utils
from connect import cursor as c 

db = utils.read("DB: ")
table = utils.read("Table: ")
id = utils.read("Delete by ID: ")

try:
    sql = """DELETE FROM {}.dbo.{} 
            WHERE ID = {}""".format(db,table,id)
    c.execute(sql)
    print(f'{id} record has been deleted')
except ConnectionError:
    print("Cannot connect to SQL Server")