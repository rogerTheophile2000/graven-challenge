import random

# 5 jares
print("Bienvenue dans le jeu !")

# compteur de clé magique
magic_keys = 0

# repeter les manches de notre jeu
while magic_keys !=3 :
    print("vous disposez de 5 jares devant vous, Choisit 1,2,3,4 ou 5")

    # choix aleatoire de la jare qui  fait perdre notre joueur
    defeat_jare = random.randint(1, 5) # nombre au hasard entre 1 et 5


    # demander de choisir le numero de la jare
    choice = int(input())

    print(f"le joueur a mit la jare numero {choice}")

    # verifications
    if choice == defeat_jare:
        print("Perdu ! vous avez choisi le jare du serpent")
        if magic_keys == 0:
            magic_keys = 0
        else:
            magic_keys -= 1
        print(f"vous avez actuellement {magic_keys} /3 clés")
    else:
        print(f"Vous avez gagner! tu obtiens une clé magique ! la jare infecté était la numéro {defeat_jare}")
        magic_keys += 1
        print(f"vous avez actuellement {magic_keys} /3 clés")

print("Tu deviens le roi du temple !")