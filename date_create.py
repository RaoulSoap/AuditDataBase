import os

def is_source_file_newer(saveFile, pathFile):
    # Obtenir la date de modification du fichier dans saveFile
    save_mtime = os.path.getmtime(saveFile)

    # Parcourez les fichiers du répertoire de pathfile
    for folder, files in os.walk(pathFile):
        for file in files:
            source_file_path = os.path.join(folder, file)
            source_mtime = os.path.getmtime(savefile_path)

            # Comparez les dates de modification
            if save_mtime > source_mtime:
                return True  # Le fichier résultat est plus récent que le fichier source

    return False  # Aucun fichier source n'est plus ancien que le fichier résultat

# Chemins vers les répertoires source et résultat
pathFile = r"C:\Users\NHNF8601\Documents\projetsPython\Base_client_FTTx\sourceFiles"
saveFile = r"C:\Users\NHNF8601\Documents\projetsPython\Base_client_FTTx\resultFiles"


if is_source_file_newer(saveFile, pathFile):
    print("Le fichier result est plus récent que les fichiers sources.")
else:
    print("Merci d'uploader des fichiers plus récent svp !.")
