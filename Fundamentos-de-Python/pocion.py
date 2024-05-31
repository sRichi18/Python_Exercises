import random

hp = 50
difficulty = 3

potion_hp = int(random.randint(25, 50) / difficulty)

hp = hp + potion_hp

print(hp)
