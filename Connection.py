import mysql.connector
print('hola')
connection = mysql.connector.connect(
    host = 'localhost',
    user = 'mopa',
    passwd = 'mopa251946'
)
print('db: ', connection)

db = connection.cursor()

db.execute("USE almacen")

db.execute("SHOW TABLES")

tables = db.fetchall()
print('Tables:')
print(tables)
# for tableDB in db:
#     print('name: ',tableDB)
#     pass

r = open('/home/oswaldo/UPCH/NovenoCuatrimestre/SOA/C2/A1/mysql.txt','r')#para almacenar el archivo
content = r.read()
w = open('/home/oswaldo/UPCH/NovenoCuatrimestre/SOA/C2/A1/mysql.txt','w')#write

w.write(content + '\nTABLE : ' + str(tables))
w.close()