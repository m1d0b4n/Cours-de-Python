from modules.Mod_exo_1 import detect_ip_version
from modules.Mod_exo_4 import lister_contenu_dossier, copier_fichier_avec_date, compter_fichiers_dans_dossier
from modules.file_manager import GestionnaireFichiers
from modules.Mod_exo_6 import (
    exporter_infos_systeme_json,
    exporter_processus_json,
    afficher_gros_processus_seulement
)

def menu():
    print("\n=== MENU PRINCIPAL ===")
    print("1. Détecter version d'une adresse IP")
    print("2. Lister les fichiers d’un dossier")
    print("3. Copier un fichier avec date (fonction)")
    print("4. Utiliser la classe GestionnaireFichiers")
    print("5. Exporter les infos système (Exo 6 - Q1)")
    print("6. Exporter tous les processus (Exo 6 - Q2)")
    print("7. Afficher processus > 2% RAM (Exo 6 - Q3)")
    print("8. Quitter")

while True:
    menu()
    choix = input("Choisissez une option (1-8) : ")

    if choix == "1":
        ip = input("Entrez une adresse IP : ")
        version = detect_ip_version(ip)
        if version == 0:
            print("Adresse IP invalide.")
        else:
            print(f"C'est une adresse IPv{version} valide.")

    elif choix == "2":
        dossier = input("Entrez le chemin du dossier à lister : ")
        fichiers = lister_contenu_dossier(dossier)
        print("Contenu du dossier :")
        for f in fichiers:
            print(" -", f)

    elif choix == "3":
        source = input("Entrez le chemin du fichier à copier : ")
        destination = input("Entrez le dossier de destination : ")
        resultat = copier_fichier_avec_date(source, destination)
        if resultat:
            print(f"Fichier copié dans : {resultat}")

    elif choix == "4":
        dossier = input("Entrez le dossier à utiliser avec la classe : ")
        gestionnaire = GestionnaireFichiers(dossier)

        print("  a) Copier un fichier")
        print("  b) Compter les fichiers")
        sous_choix = input("  Choisissez (a/b) : ")

        if sous_choix == "a":
            fichier = input("  Entrez le chemin du fichier à copier : ")
            res = gestionnaire.copier_fichier(fichier)
            if res:
                print(f"  Fichier copié dans : {res}")
        elif sous_choix == "b":
            count = gestionnaire.compter_fichiers()
            print(f"  Il y a {count} fichiers dans le dossier.")
        else:
            print("  Option invalide.")

    elif choix == "5":
        fichier = input("Entrez le nom du fichier de sortie JSON : ")
        exporter_infos_systeme_json(fichier)
        print(f"Infos système exportées dans {fichier}")

    elif choix == "6":
        fichier = input("Entrez le nom du fichier de sortie JSON : ")
        exporter_processus_json(fichier)
        print(f"Processus exportés dans {fichier}")

    elif choix == "7":
        print("Voici les processus qui utilisent plus de 2% de RAM :")
        afficher_gros_processus_seulement()

    elif choix == "8":
        print("Au revoir ! 👋")
        break

    else:
        print("Option invalide, réessayez.")
