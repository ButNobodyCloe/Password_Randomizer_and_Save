# Choix de la longueur du mot de passe

import string
import random



# caractères pour générer un mot de passe

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")


def generate_random_password():
    longueur = int(input("quelle taille de mot de passe : "))

    # Melanger les caractères
    random.shuffle(characters)

    # Prendre des caractères aléatoires dans la liste
    password = []
    for i in range(longueur):
        password.append(random.choice(characters))

    # Mélanger le résultat du mot de passe
    random.shuffle(password)

    # Afficher le mot de passe
    mdp = ("".join(password))

    site = input("Pour quel site?")
    compte = input("Quel est l'addresse email du compte?")

    print("Voici vos informations \n site:", site, "\n compte:", compte, "\n mot de passe:", mdp, )

    file = open('mdp.txt', 'a')
    file.write("%s = %s\n" % ("site", site))
    file.write("%s = %s\n" % ("compte", compte))
    file.write("%s = %s\n" % ("mdp", mdp))
    file.close()


generate_random_password()
