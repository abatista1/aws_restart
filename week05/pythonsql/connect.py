import pyodbc

connection_str = (
    r'Driver=SQL Server;'
    r'Server=ALIENWARE;'
    r'Trusted_Connection=yes;'
    )

def createconnection(connstr):
    return pyodbc.connect(connstr,autocommit=True)

connection = createconnection(connection_str)

def createcursor(connection):
    return connection.cursor()

cursor = createcursor(connection)

def closeconnection():
    connection.close()
