import os

def rename_files(directory):
    # Parcourir tous les fichiers du répertoire
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            # Créer le nouveau nom du fichier
            new_name = filename.lower().replace('_', '-')
            base, extension = os.path.splitext(new_name)
            new_name = f"{base}_en{extension}"
            
            # Renommer le fichier
            os.rename(os.path.join(directory, filename), os.path.join(directory, new_name))
            print(f"Renamed '{filename}' to '{new_name}'")

# Spécifiez le chemin du répertoire contenant les fichiers à renommer
directory_path = 'D:/FreeDome-Data/modules/modulesIcons/phet'
rename_files(directory_path)
