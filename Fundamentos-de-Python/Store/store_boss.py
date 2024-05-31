from store_pack.book import Book
from store_pack.movie import Movie
from store_pack.stock_list import List_Stock

print("-----Welcome-----")
while True:
    print("")
    print("1 - Add Movie")
    print("2 - Movies list")
    print("3 - Add book")
    print("4 - Books lisr")
    print("5 - Watch items with few stock")
    print("6 - Exit")

    option = int(input("Choose one: (1-6)").strip())

    print("")
    m = Movie()
    b = Book()
    if option == 1:
        print("---Movie details---")
        name = input("Movie´s name: ").strip().capitalize()
        dur = input("Movie´s duration: ").strip()
        stock = int(input("Stock: ").strip())
        m.Add_Movie(name, dur, stock)

    elif option == 2:
        lst = m.Movies_List()
        print(lst)

    elif option == 3:
        print("---Book details---")
        name = input("Book´s name: ").strip().capitalize()
        pgs = int(input("Book´s pages: ").strip())
        stock = int(input("Stock: ").strip())
        b.Add_Book(name, pgs, stock)

    elif option == 4:
        lst = b.Books_List()
        print(lst)

    elif option == 5:
        stk = int(input("Quantity to evaluate: ").strip())
        lst = List_Stock(stk, m, b)
        print("---Items with stock less-than " + str(stk) + "---")
        print(lst)

    elif option == 6:
        break

    else:
        print("ERROR invalid option")
