import mysql.connector

my_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="ecommerce")

my_cursor = my_db.cursor()

sql = """ INSERT INTO cliente
            (name, last_name)
            VALUES(%s, %s) """

#values = ("Mercedes","Rojas")
#my_cursor.execute(sql, values)

values = [("Carlos","Parco"),
          ("Kyle","Smith"),
          ("Anderson","Salazar")]
my_cursor.executemany(sql, values)

my_db.commit()

my_cursor.execute("SELECT * FROM cliente")
for reg in my_cursor:
    print(reg)

my_db.close()
