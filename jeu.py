#definir la fonction choix_option
#   tant que infini
#       proposer les choix a l'utilisateur 
#       demander un choix à l'utilisateur
#       on appel la fonction conditon avec les choix 
#       si le choix est valide
#           retourner le choix

#definit la condition
#   si le choix n'est pas un chiffre 
#       afficher un message d'erreur
#       retourner false
#   convertir le choix en nombre
#   si le choix est inferieur à 1 ou supérieur à 3
#       afficher un message d'erreur
#       retouner false
#   retourner true


# Définir la fonction saisir pseudo 
#   tant que infini
#       demander à l'utilisateur de saisir son pseudo
#       si le pseudo n'est pas vide
#           retourner le pseudo
#       sinon
#           afficher un message d'erreur  


# Définir le choix du personnage aléatoire
#   parmis la liste personnage dans le model
#   choisir un  au hasard dans la liste personnage
#   retourner le personnage choisi  

# Définir le choix du monstre aléatoie
#   parmis la liste monstre dans le model
#   choisir un monstre au hasard dans liste_monstre
#   retourner le monstre choisi 


#Définir la fonction attaquer
#   personnage attaque le monstre
#   retirer les dégâts du personnage aux PV du monstre
#   afficher personnage ATK monstre avec les degats 
#   montrer les pv du monstre
#   si est_mort retourner true 
#        arreter la fonction
#   monstre attaque le personnage
#   retirer les dégâts du monstre aux PV du personnage
#   afficher monstre ATK personnage avec les degats 
#   montrer les pv du personnage
#   si est_mort retourner true 


# Définir la fonction est_mort 
#   si les PV du monstre sont inférieurs ou égaux à 0
#       afficher que le personnage a gagné
#       return true
#   si les PV du personnage sont inférieurs ou égaux à 0
#       afficher que le monstre a gagné 
#       return true
#   sinon 
#       retourner false


#Définir la fonction combat
#   annoncer le combat entre le personnage et le monstre
#   tant que les pv du personnage sont superieur a 0
#       et que les PV du monstre sont supérieurs à 0
#           appeler la fonction attaquer

# Définir la fonction main
#   tant que infini
#       appeler choix utilisateur et récupérer les choix
#       si le choix est 1
#           appeler saisir_pseudo
#           appeler choix_personnage_aleatoire
#           appeler choix_monstre_aleatoire
#           appeler combat avec le personnage et le monstre
#       sinon si le choix est 2
#           afficher le leaderboard
#       sinon si le choix est 3
#           afficher quitter
#           arrêter la boucle

# Lancer le programme 
#   appeler main



from pymongo import MongoClient
from model import personnage, monstre

client = MongoClient("mongodb://localhost:27017/")
db = client["bdd_python"]

def choix_option():
    while True: 
        print("1 - Jouer")
        print("2 - Affichet le leaderboard")
        print("2 - quitter")
        choix = input("Ton choix : ").strip()
        if condition(choix):
            return int(choix)

def condition():
    if not choix_option.isdigit():
        print("veuillez rentrer un chiffre parmis les options proposé")
        return False
    choix = int(choix)
    if choix < 1 or choix > 3:
        print("veuillez rentrer un chiffre parmis les options proposé")
        return False
    return True

    



#definit la condition
#   si le choix n'est pas un chiffre 
#       afficher un message d'erreur
#       retourner false
#   convertir le choix en nombre
#   si le choix est inferieur à 1 ou supérieur à 3
#       afficher un message d'erreur
#       retouner false
#   retourner true
        

    








