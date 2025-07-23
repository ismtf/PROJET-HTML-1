# Demander une phrase à l'utilisateur
phrase = input("Entrez une phrase qui se termine par un point : ")

# Initialisation des compteurs
longueur = 0
nb_mots = 1  # On suppose qu'il y a au moins un mot
nb_voyelles = 0

# Liste des voyelles (majuscules et minuscules)
voyelles = "aeiouyAEIOUY"

# Parcours de chaque caractère de la phrase
for caractere in phrase:
    longueur += 1
    if caractere in voyelles:
        nb_voyelles += 1
    if caractere == " ":
        nb_mots += 1

# Affichage des résultats
print("Longueur de la phrase :", longueur)
print("Nombre de mots :", nb_mots)
print("Nombre de voyelles :", nb_voyelles)===
