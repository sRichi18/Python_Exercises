import mysql.connector

my_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="ecommerce")

my_cursor = my_db.cursor()

#sql = """SELECT * FROM cliente"""

#sql = """SELECT name, last_name FROM cliente"""

#sql = """SELECT name, last_name FROM cliente
#            WHERE name = 'Maria'"""

sql = """SELECT name, last_name FROM cliente
            WHERE name = %s"""

my_cursor.execute(sql, ("Pedro",))
for reg in my_cursor:
    print(reg)

my_db.close()
