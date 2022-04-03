from connect import cursor as c 
import utils

db = utils.read("DB: ")
table = utils.read("Table: ")

try:
    sql = "SELECT * FROM {}.dbo.{}".format(db,table)
    c.execute(sql)
    result = c.fetchall()
    for line in result:
        print(line)
except ConnectionError:
    print("Cannot connect to SQL Server")