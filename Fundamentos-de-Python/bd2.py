import mysql.connector

my_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="ecommerce")

my_cursor = my_db.cursor()

sql = """ CREATE TABLE cliente(
            name VARCHAR(255),
           last_name VARCHAR(255)) """

my_cursor.execute(sql)

#sql = "DROP TABLE IF EXISTS cliente"
#my_cursor.execute(sql)

my_cursor.execute("SHOW TABLES")
for tables in my_cursor:    
    print(tables)

my_db.close()
