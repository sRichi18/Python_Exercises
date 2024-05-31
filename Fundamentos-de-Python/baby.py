from random import choice

cuestions = [
        "Porque el cielo es azul?: ",
        "Porque hay una cara en la luna?: ",
        "Donde estan los dinosaurios?: "
    ]

ask = choice(cuestions)

answer = input(ask).lower().strip()

while answer != "porque si":
    answer = input("Porque?: ").strip().lower()

print("Oh... ok")
