#ask for name
name =  input("Tell me your name: ")

#ask for age
age = int(input("Tellme your age: "))

#ask for te addres
address = input("What city you live? ")

#ask for hobbie
hobbie = input("What is your hobbie? ")

#create ouput text
#greeting =  f"Hi! {name} , your age is {age}, you live in {address} and your hobbie is {hobbie}"
string  = "Hi! {} , your age is {}, you live in {} and your hobbie is {}"
greeting = string.format(name, age, address, hobbie)

#print text on screen
print(greeting)
