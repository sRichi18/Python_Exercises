#from movie import Movie
#from book import Book

#m = Movie()
#b = Book()

#m.Add_Movie("Tarzan","1:25:00",15)
#m.Add_Movie("Bourne","1:35:03",3)
#m.Add_Movie("El Hobbit","1:40:00",20)
#m.Add_Movie("Rambo","1:43:00",6)
#b.Add_Book("Math I",120,13)
#b.Add_Book("Math II",100,21)
#b.Add_Book("Math III",90,26)
#b.Add_Book("Math IV",95,14)

def List_Stock(stock_number, obj_m, obj_b):
    items_list = []
    new_list = []

    for mv in obj_m.Movies_List():
        items_list.append(mv)

    for bk in obj_b.Books_List():
        items_list.append(bk)

    for item in items_list:
        if stock_number >= item["Stock"]:
            new_list.append(item)

    return new_list

#print(List_Stock(14))
