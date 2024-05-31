known_users = ["Alice", "Bob", "Dan", "Emma", "Fred", "Georgie", "Harry"]
print(len(known_users))

while True:
    print("Hi my name is Teto")
    name = input("What is your name?:").strip().capitalize()

    if name in known_users:
        print("Hi {}!".format(name))
        delete = input("Do you want to be delete from the system? (y/n)")

        if delete == "y":
            known_users.remove(name)
        elif delete == "n":
            print("No problem if you don´t want to")
        
    else:
        print("Hmm... I don´t known you {}".format(name))
        add = input("Do you want to be added to the system? y/n")

        if add == "y":
            known_users.append(name)
        elif add == "n":
            print("No problem if you don´t want to")
