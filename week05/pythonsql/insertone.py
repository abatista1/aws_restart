from connect import cursor as c 
import utils

db = utils.read("DB: ")
table = utils.read("Table: ")

try:
    sql = """INSERT INTO {}.dbo.{} 
    VALUES(100001,'John Rambo',100,'HD')""".format(db,table)
    c.execute(sql)
    print(f'A new record has been created!!!')
except ConnectionError:
    print("Cannot connect to SQL Server")