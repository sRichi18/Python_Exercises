
books = []

class Book:
    def __init__(self, name="", pages=0, stock=0):
        self.name = name
        self.pages = pages
        self.stock = stock

    def Add_Book(self, name, pages, stock):
        self.name = name
        self.pages = pages
        self.stock = stock
        books.append({"Movie": name,
                       "Pages": pages,
                       "Stock": stock})

    def Books_List(self):
        return books

#l = Book()
#l.Add_Book("Matematicas I",100,23)
#l.Add_Book("Programacion",87,12)

#print(l.Books_List())
