import os
import shutil
from datetime import datetime
import argparse

def lister_et_copier(fichier):
    """
    Liste le contenu du dossier de travail et copie le fichier spécifié.
    La copie aura dans son nom la date et l'heure de la copie.
    """
    # Lister le contenu du dossier de travail courant
    print("Contenu du dossier de travail :")
    contenus = os.listdir('.')
    for element in contenus:
        print(element)
    
    # Vérifier que le fichier existe
    if not os.path.isfile(fichier):
        print(f"Le fichier '{fichier}' n'existe pas dans le dossier de travail.")
        return
    
    # Créer un nom de copie avec la date et l'heure
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    nom_base, extension = os.path.splitext(fichier)
    copie_nom = f"{nom_base}_{timestamp}{extension}"
    
    # Copier le fichier
    shutil.copy(fichier, copie_nom)
    print(f"Le fichier '{fichier}' a été copié en '{copie_nom}'.")

def compter_fichiers(dossier):
    """
    Compte le nombre de fichiers (excluant les dossiers)
    dans le dossier passé en argument.
    """
    try:
        items = os.listdir(dossier)
    except Exception as e:
        print(f"Erreur lors de l'ouverture du dossier '{dossier}': {e}")
        return 0

    count = 0
    for item in items:
        chemin = os.path.join(dossier, item)
        if os.path.isfile(chemin):
            count += 1
    return count

if __name__ == "__main__":
    # Définition des arguments du script
    parser = argparse.ArgumentParser(
        description="Script pour lister le contenu, copier un fichier et compter le nombre de fichiers dans un dossier."
    )
    parser.add_argument(
        "-d", "--directory", 
        help="Dossier dans lequel compter les fichiers (par défaut, le dossier de travail actuel)",
        default="."
    )
    parser.add_argument(
        "-f", "--file", 
        help="Nom du fichier à copier (par défaut, 'exemple.txt')",
        default="exemple.txt"
    )
    
    args = parser.parse_args()
    
    # Partie 1 : Lister et copier un fichier
    lister_et_copier(args.file)
    
    # Partie 2 et 3 : Compter le nombre de fichiers dans le dossier spécifié
    nb_fichiers = compter_fichiers(args.directory)
    print(f"Nombre de fichiers dans le dossier '{args.directory}': {nb_fichiers}")
