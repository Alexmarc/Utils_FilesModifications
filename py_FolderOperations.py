from os import listdir
from os.path import isfile, join
from os import walk

filePath = f"D:\\AlexandreMarchettiDossierPersonnel\\__GITHUB_PROJECT__\\Utils_FilesModifications\\TestFolder"


def GetFilesInsideFolder (_filePath) :
    fichiers = [f for f in listdir(_filePath) if isfile(join(_filePath, f))]
    print(fichiers)


def GetFilesInFolderAndSubfolder (_filePath) :
    listeFichiers = []
    listeDossier = []

    for (repertoire, sousRepertoires, fichiers) in walk(_filePath):
        listeFichiers.extend(fichiers) 
        listeDossier.extend(repertoire)
        print(fichiers)
        print(sousRepertoires)


GetFilesInFolderAndSubfolder(filePath)