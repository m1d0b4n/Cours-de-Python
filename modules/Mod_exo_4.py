import os
import shutil
from datetime import datetime

def lister_contenu_dossier(dossier):
    try:
        return os.listdir(dossier)
    except FileNotFoundError:
        print("Le dossier n'existe pas.")
        return []
    except Exception as e:
        print(f"Erreur : {e}")
        return []

def copier_fichier_avec_date(fichier_source, dossier_destination):
    try:
        date_str = datetime.now().strftime("%Y%m%d_%H%M%S")
        nom_fichier = os.path.basename(fichier_source)
        nouveau_nom = f"{date_str}_{nom_fichier}"
        chemin_destination = os.path.join(dossier_destination, nouveau_nom)
        shutil.copy2(fichier_source, chemin_destination)
        return chemin_destination
    except Exception as e:
        print(f"Erreur lors de la copie : {e}")
        return None

def compter_fichiers_dans_dossier(dossier):
    try:
        return len([f for f in os.listdir(dossier) if os.path.isfile(os.path.join(dossier, f))])
    except Exception as e:
        print(f"Erreur : {e}")
        return 0
