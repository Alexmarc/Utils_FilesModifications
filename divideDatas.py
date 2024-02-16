import re


txtFilePath = input("Please enter file path: ")
outputTxtFilePath = input("Please enter output file path: ")

# Ouvrir le fichier en mode lecture
with open(txtFilePath, "r") as fichier:
    contenu = fichier.read()

ratio = 0.1
newContent = ""
lines = contenu.split("\n")

for j in range(len(lines)):
    line = lines[j]
    nums = line.strip().split(" ")
    for i in range(len(nums)):
        num = float(nums[i]) * ratio
        newContent += str(num) + " " if i <len(nums)-1 else ""
    newContent+="\n" if j == len(lines)-1 else ""

# Ouvrir le fichier en mode écriture et écrire le contenu modifié
with open(outputTxtFilePath, "w") as fichier:
    fichier.write(newContent)
