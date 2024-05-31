import mysql.connector

my_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="ecommerce")

my_cursor = my_db.cursor()

sql = """ALTER TABLE cliente
            ADD ciente_id INT AUTO_INCREMENT PRIMARY KEY """

my_cursor.execute(sql)

my_cursor.execute("DESCRIBE cliente")

for columns in my_cursor:
    print(columns)

my_db.close()
