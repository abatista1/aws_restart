from connect import cursor as c 
import utils

db = utils.read("DB: ")
table = utils.read("Table: ")
id = utils.read("Find by ID: ")

try:
    sql = "SELECT * FROM {}.dbo.{} WHERE ID = {}".format(db,table,id)
    c.execute(sql)
    result = c.fetchall()
    for line in result:
        print(line)
except ConnectionError:
    print("Cannot connect to SQL Server")