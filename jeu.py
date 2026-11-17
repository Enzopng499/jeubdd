menu boucle 

# Afficher le menu
#   tant que infini
#    proposer les choix a l'utilisateur  
#    demander un choix à l'utilisateur
#    si le choix est valide = 1,2 ou 3 
#   si choix n'est pas isdighit
#   return false
#   sinon
#    arreter la boucle ici
#       sinon
#           afficher un message d'erreur 
#           la boucle continue 
...



# Définir le pseudo du joueur
#       demander à l'utilisateur de saisir son pseudo
#       si le pseudo n'est pas vide
#       retourner le pseudo
#       sinon
#           afficher un message d'erreur


# Définir le choix du personnage aléatoire
#   choisir un personnage au hasard dans personnage
#   retourner le personnage choisi


# Définir le choix du monstre aléatoire
#   choisir un monstre au hasard dans liste_monstre
#   retourner le monstre choisi


# Définir la fonction combat entre un personnage et un monstre
#   annoncer le combat entre personnage et el monstro
#   créer une variable round = 0
#   tant que les pv du personnage sont superieur a 0
#       et que les PV du monstre sont supérieurs à 0
#       combat continue

#   le personnage attaque le monstre
#   retirer les dégâts aux PV du monstre
#   si les PV du monstre sont inférieurs ou égaux à 0
#   afficher que le personnage a gagné
#   arrêter la boucle breakj
#   le monstre attaque le personnage
#   retirer les dégâts aux PV du personnage
#   si les PV du personnage sont inférieurs ou égaux à 0
#           afficher que le monstre a gagné
#   arrêter la boucle break



from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client 

def main():
    afficher_menu()







