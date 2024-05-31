path = "test.txt"

try:
    file = open(path)
except Exception as err:
    print("Error opening file: ", err)
else:
    print("File open, continue...")
finally:
    print("Final process, bye...")
