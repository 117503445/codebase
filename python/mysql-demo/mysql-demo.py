import mysql.connector
import config

mydb = mysql.connector.connect(
    host=config.mysql_host,
    port=config.mysql_port,
    user=config.mysql_username,
    password=config.mysql_password,
    database='mydb'
)
cursor = mydb.cursor()

sql = f"SELECT * from mytable"
cursor.execute(sql)

for r in cursor:
    print(r)