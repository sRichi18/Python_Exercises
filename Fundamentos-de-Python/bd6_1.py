import mysql.connector

my_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="ecommerce")

my_cursor = my_db.cursor()

sql = """ UPDATE cliente
           SET name = %s
           WHERE name = %s """

values =  ("Juan", "Anderson")
my_cursor.execute(sql, values)
my_db.commit()

my_cursor.execute("SELECT * FROM cliente")
for reg in my_cursor:
    print(reg)


my_db.close()
