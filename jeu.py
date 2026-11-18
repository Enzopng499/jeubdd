#definir la fonction menu
#   afficher menu
#   tant que infini
#       proposer les choix a l'utilisateur 
#       demander un choix à l'utilisateur
#       on appel la condition
#       si le choix est valide
#           arreter la boucle 
#   retourner le choix

#definit la condition
#   si le choix n'est pas un chiffre 
#       afficher un message d'erreur
#       retourner false
#   convertir le choix en nombre
#   si le choix est inferieur à 1 ou supérieur à 3
#       afficher un message d'erreur
#       retouner false



# Définir le pseudo du joueur
#       demander à l'utilisateur de saisir son pseudo
#       si le pseudo n'est pas vide
#           retourner le pseudo
#       sinon
#           afficher un message d'erreur


# Définir le choix du personnage aléatoire
#   choisir un personnage au hasard dans personnage
#   retourner le personnage choisi


# Définir le choix du monstre aléatoie
#   choisir un monstre au hasard dans liste_monstre
#   retourner le monstre choisi



# Définir la fonction combat entre un personnage et un monstre
#   annoncer le combat entre personnage et el monstro
#   le personnage attaque le monstre
#   retirer les dégâts aux PV du monstre
#   si les PV du monstre sont inférieurs ou égaux à 0
#       afficher que le personnage a gagné
#       arrêter la boucle break
#   le monstre attaque le personnage
#   retirer les dégâts aux PV du personnage
#   si les PV du personnage sont inférieurs ou égaux à 0
#       afficher que le monstre a gagné 
#       arrêter la boucle 




#Définir la fonction attaquer 
#   personnage attaque le monstre
#   retirer les dégâts de l'attaquant aux PV du monstre
#   montrer les pv du monstre
#   monstre attaque le personnage
#   retirer les dégâts du defensseur aux PV de l'attaquant
#   montrer les pv de l'attanquant
#   afficher qui attaque qui et combien de dégâts

# Définir la fonction est_mort 
#   si les PV du monstre sont inférieurs ou égaux à 0
#       afficher que le personnage a gagné
#       return true
#   si les PV du personnage sont inférieurs ou égaux à 0
#       afficher que le monstre a gagné 
#       return true

#Définir la fonction antité vivante
#   annoncer le combat entre le personnage et le monstre 
#   tant que les pv du personnage sont superieur a 0
#       et que les PV du monstre sont supérieurs à 0
#       continuer le combat





from pymongo import MongoClient
from model import personnage, monstre

client = MongoClient("mongodb://localhost:270er que le monstre a gagné17/")
db = client["bdd_python"]

def main():
    afficher_menu()








