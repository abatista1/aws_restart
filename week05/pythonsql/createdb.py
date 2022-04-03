from connect import cursor as c 
import utils

db = utils.read("Create DB: ")

try:
    sql = "CREATE DATABASE {}".format(db)
    c.execute(sql)
    print(f'{db} has been created!!!')
except ConnectionError:
    print("Cannot connect to SQL Server")