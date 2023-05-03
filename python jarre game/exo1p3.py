import random

# 5 jares
print("Bienvenue dans le jeu !")

#choix du parametrage/ niveau de fdificulté
print("Ecrit 1:facile, 2:moyen, 3:difficile")
niveau_jeux = int(input())

# compteur de clé magique
magic_keys = 0

# repeter les manches de notre jeu
while magic_keys !=3 :
    print("vous disposez de 5 jares devant vous, Choisit 1,2,3,4 ou 5")

    #tablrau aui va contenit chacune des jarres
    jares = ['K', 'K', 'K', 'K', 'K', 'K']

    # boucle aui va tourner de fois au'il doit y avoir dea serpents
    for i in range(1, niveau_jeux):
        print("1 serpent a été ajouté dans une jarre")
        jares[i]='S'
    random.shuffle(jares)
    print(jares)

    # demander de choisir le numero de la jare
    choice = int(input())

    print(f"le joueur a mit la jare numero {choice}")

    # verifications
    if jares[choice]=='S':
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