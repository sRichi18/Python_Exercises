import string

#Obtener la oracion del usuario
original = input("Ingresa una oracion: ").strip().lower()

#Dividir la oracion en palabras
words = original.split()

#Recorrer las palabras con el traductor
new_words = []
for word in words:
    if word[0] in "aeiou":
        new_words = word + "yey" #Comienza con una vocal, agrega yey

    else:
        vocal_pos = 0
        for letter in word:
            if letter not in "aeiou":
                vocal_pos = vocal_pos + 1
            else:
                break
        cons = word[:vocal_pos]
        rest = word[vocal_pos:]
        new_word = rest + cons + "ay"
        new_words.append(new_word) #??? no se por que me splitea la palabra T.T

#Unir las palabras en una oracion
ext = " ".join(new_words)


#Generar cadena final
print(ext)
