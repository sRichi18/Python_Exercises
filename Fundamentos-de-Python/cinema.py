movies = {
        "Nemo": [3, 5],
        "Simios": [18, 5],
        "Tarzan": [12, 5],
        "Ded Pool": [16, 5],
    }

while True:
    selec = input("Que pelicula deseas ver?:").strip().title()

    #Pelicula en existencia?
    if selec in movies:
        age = int(input("Cuantos años tienes?:").strip())
        tickets = movies[selec][1]
        
        #Verificando edad
        if age >= movies[selec][0]:

            #Verificando si aun existen voletos
            if tickets > 0:
                print("Disfruta la pelicula")
                movies[selec][1] =  movies[selec][1] - 1
            else:
                print("Voletos agotados")
            
        else:
            print("No tienes la edad suficiente para ver esta pelicula")
    else:
        print("No tenemos esa pelicula")

#Presina Ctrl + c si deseas detener el bucle while desde el teclado
