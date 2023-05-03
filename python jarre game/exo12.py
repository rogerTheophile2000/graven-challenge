import random

# choisir le niveau
level = int(input("Quel niveau de difficulte pour le jeux ? 1, 2, 3\n"))

# on genere autant de serpents que le niveau
snakes = ['S'] * level

# on regarde combien de jarees ne sont pas infectees
difference = 5 - level

# on genere les cles 
keys = ['K'] * difference


jares = keys + snakes

random.shuffle(jares)
print(jares)
print(snakes)
print(keys)