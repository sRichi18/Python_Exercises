path = "C:/Users/LENOVO/Desktop/Fundamentos de Python/Files/person.txt"

def Add(name, age, gender):
    with open(path, "a") as file:
        row = "{},{},{}\n".format(name,age,gender)
        file.write(row)
        print("----Person added-----")

def List():
    with open(path, "r") as file:
        print("-----List-----")
        print(file.read())
        print("-" * 10)

def List_Genre(letter_genre):
    with open(path, "r") as files:
        files.seek(0,0)
        
        for file in files:
            file = file.strip("\n")
            name, age, gender = file.split(",")

            if letter_genre == gender:
                print(file)

while True:
    print("---Choose an option")
    print("1 - Add a person")
    print("2 - List people")
    print("3 - List people by gender")
    print("4 - Exit")
    option = input("Selec (1-4): ").strip()

    if int(option) == 1:
        nam = input("Your name: ").strip().capitalize()
        age = input("Your age: ").strip()
        gen = input("Your gender: ").strip().upper()
        Add(nam, age, gen)

    elif int(option) == 2:
        List()

    elif int(option) == 3:
        gen = input("Enter the gender: ").strip().upper()
        List_Genre(gen)

    elif int(option) == 4:
        break

    else:
        print("Invalid option")

    
