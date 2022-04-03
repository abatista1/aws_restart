from connect import cursor as c 
import utils

db = utils.read("DB: ")
table = utils.read("Delete Table: ")

try:
    sql = "DROP TABLE {}.dbo.{}".format(db,table)
    c.execute(sql)
    print(f'{table} has been deleted!!!')
except ConnectionError:
    print("Cannot connect to SQL Server")