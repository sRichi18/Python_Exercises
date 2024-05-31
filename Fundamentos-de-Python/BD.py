import mysql.connector

my_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root")

my_cursor = my_db.cursor()

#sql = "CREATE DATABASE ecommerce"
#my_cursor.execute(sql)

#sql = "DROP DATABASE escuela"
#my_cursor.execute(sql)

sql = "SHOW DATABASES"
my_cursor.execute(sql)

for items in my_cursor:
    print(items)

my_db.close()
