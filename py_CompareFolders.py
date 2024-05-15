import os
import filecmp
from pathlib import Path

def list_files(directory):
    """ Renvoie un dictionnaire des fichiers dans le répertoire donné, où la clé est le nom du fichier et la valeur est le chemin complet. """
    return {file.name: file for file in Path(directory).rglob('*') if file.is_file()}

def compare_folders(folder1, folder2):
    # Récupérer les fichiers de chaque dossier
    files1 = list_files(folder1)
    files2 = list_files(folder2)

    # Noms de fichiers dans chaque dossier
    names1 = set(files1.keys())
    names2 = set(files2.keys())

    # Fichiers uniquement dans chaque dossier
    only_in_folder1 = names1 - names2
    only_in_folder2 = names2 - names1

    # Fichiers communs aux deux dossiers
    common_names = names1 & names2

    # Comparer le contenu des fichiers communs
    same_files = []
    diff_files = []
    for name in common_names:
        file1 = files1[name]
        file2 = files2[name]
        if filecmp.cmp(file1, file2, shallow=False):
            same_files.append(name)
        else:
            diff_files.append(name)

    return only_in_folder1, only_in_folder2, same_files, diff_files

# Chemins des deux dossiers à comparer
folder_path1 = 'D:/AlexandreMarchettiDossierPersonnel/__GITHUB_PROJECT__/Utils_FilesModifications/CompareFolderTest/Test1'
folder_path2 = 'D:/AlexandreMarchettiDossierPersonnel/__GITHUB_PROJECT__/Utils_FilesModifications/CompareFolderTest/Test2'

# Appel de la fonction de comparaison
results = compare_folders(folder_path1, folder_path2)
print("Fichiers uniquement dans", folder_path1, ":", results[0])
print("Fichiers uniquement dans", folder_path2, ":", results[1])
print("Fichiers identiques dans les deux dossiers:", results[2])
print("Fichiers avec des différences:", results[3])
