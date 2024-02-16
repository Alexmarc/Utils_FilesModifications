import re

txtFilePath = input("Please enter file path: ")
outputTxtFilePath = input("Please enter output file path: ")

# Ouvrir le fichier en mode lecture
with open(txtFilePath, "r") as fichier:
    contenu = fichier.read()

# Utiliser une expression régulière pour trouver et supprimer les chaînes entre guillemets
contenu_modifie = re.sub(r'"[^"]*"', '', contenu)

# Ouvrir le fichier en mode écriture et écrire le contenu modifié
with open(outputTxtFilePath, "w") as fichier:
    fichier.write(contenu_modifie)
