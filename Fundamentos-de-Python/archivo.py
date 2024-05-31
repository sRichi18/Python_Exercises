path = "C:/Users/LENOVO/Desktop/Fundamentos de Python/archivos/data.txt"
path2 = "C:/Users/LENOVO/Desktop/Fundamentos de Python/archivos/schl_data.txt"

schl_archive = open(path2, "r+")

schl_archive.seek(0, 2)
schl_archive.write("walter")


schl_archive.close()
