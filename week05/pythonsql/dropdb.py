from connect import cursor as c 
import utils

db = utils.read("Drop DB: ")

try:
    sql = "DROP DATABASE {}".format(db)
    c.execute(sql)
    print(f'{db} has been deleted!!!')
except ConnectionError:
    print("Cannot connect to SQL Server")