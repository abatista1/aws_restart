from connect import cursor as c 
import utils

db = utils.read("DB: ")
table = utils.read("Table: ")
file = utils.read("Load File: ")

try:
    sql = """BULK INSERT {}.dbo.{}
    FROM {}
    WITH(FIRSTROW = 2, FIELDTERMINATOR= ',',ROWTERMINATOR = '\n')""".format(db,table,file)
    c.execute(sql)
    print(f'{file} data has been loaded into {table}')
except ConnectionError:
    print("Cannot connect to SQL Server")