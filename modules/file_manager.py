import os
import shutil
from datetime import datetime

class GestionnaireFichiers:
    def __init__(self, dossier):
        self.dossier = dossier

    def copier_fichier(self, fichier_source):
        try:
            date_str = datetime.now().strftime("%Y%m%d_%H%M%S")
            nom_fichier = os.path.basename(fichier_source)
            nouveau_nom = f"{date_str}_{nom_fichier}"
            destination = os.path.join(self.dossier, nouveau_nom)
            shutil.copy2(fichier_source, destination)
            return destination
        except Exception as e:
            print(f"Erreur lors de la copie : {e}")
            return None

    def compter_fichiers(self):
        try:
            return len([
                f for f in os.listdir(self.dossier)
                if os.path.isfile(os.path.join(self.dossier, f))
            ])
        except Exception as e:
            print(f"Erreur : {e}")
            return 0
