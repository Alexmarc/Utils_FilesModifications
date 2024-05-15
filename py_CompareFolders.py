import os
import filecmp
from pathlib import Path

def list_files(directory):
    """ Renvoie une liste des chemins de fichiers dans le répertoire donné. """
    return {file for file in Path(directory).rglob('*') if file.is_file()}

def compare_folders(folder1, folder2):
    # Récupérer les fichiers de chaque dossier
    files1 = list_files(folder1)
    files2 = list_files(folder2)

    # Fichiers uniquement dans chaque dossier
    only_in_folder1 = files1 - files2
    only_in_folder2 = files2 - files1

    # Fichiers communs aux deux dossiers
    common_files = files1.intersection(files2)

    # Comparer le contenu des fichiers communs
    same_files = []
    diff_files = []
    for file in common_files:
        # On compare les fichiers qui ont le même nom
        if filecmp.cmp(folder1 / file, folder2 / file, shallow=False):
            same_files.append(file)
        else:
            diff_files.append(file)

    return only_in_folder1, only_in_folder2, same_files, diff_files

# Utiliser la fonction pour comparer deux dossiers
folder_path1  = 'D:/AlexandreMarchettiDossierPersonnel/__GITHUB_PROJECT__/Utils_FilesModifications/CompareFolderTest/Test1'
folder_path2  = 'D:/AlexandreMarchettiDossierPersonnel/__GITHUB_PROJECT__/Utils_FilesModifications/CompareFolderTest/Test2'


# Appel de la fonction de comparaison
results = compare_folders(folder_path1, folder_path2)
print("Fichiers uniquement dans le premier dossier:", results[0])
print("Fichiers uniquement dans le deuxième dossier:", results[1])
print("Fichiers identiques dans les deux dossiers:", results[2])
print("Fichiers avec des différences:", results[3])
