
movies = []

class Movie:
    def __init__(self, name="", duration="", stock=0):
        self.name = name
        self.duration = duration
        self.stock = stock

    def Add_Movie(self, name, duration, stock):
        self.name = name
        self.duration = duration
        self.stock = stock
        movies.append({"Movie": name,
                       "Duration": duration,
                       "Stock": stock})

    def Movies_List(self):
        return movies

#p = Movie()
#p.Add_Movie("Tarzan","1:35:00",21)
#p.Add_Movie("Rambo","1:32:00",12)

#print(p.Movies_List())
