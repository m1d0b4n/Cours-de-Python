from modules.Mod_exo_1 import detect_ip_version
from modules.Mod_exo_4 import lister_contenu_dossier, copier_fichier_avec_date, compter_fichiers_dans_dossier
from modules.file_manager import GestionnaireFichiers
from modules.Mod_exo_6 import (
    exporter_infos_systeme_json,
    exporter_processus_json,
    afficher_gros_processus_seulement
)
from modules.Mod_exo_7 import (
    lire_fichier_dynamique,
    filtrer_boolean_yes,
    filtrer_url_reddit,
    pourcentage_conditions,
    exporter_df
)
from modules.ascii_art import afficher_logo
from modules.menu import menu
from modules.Mod_exo_8 import lister_interfaces_reseau_local, lister_interfaces_reseau_distant

# Affiche l'ASCII une seule fois au lancement
afficher_logo()

while True:
    menu()
    choix = input("❓ Choisissez une option (1-9) : ")

    if choix == "1":
        ip = input("❓ Entrez une adresse IP : ")
        version = detect_ip_version(ip)
        print(f"✅ C'est une adresse IPv{version} valide." if version else "Adresse IP invalide.")

    elif choix == "2":
        dossier = input("❓ Entrez le chemin du dossier à lister : ")
        fichiers = lister_contenu_dossier(dossier)
        print("✅ Contenu du dossier :")
        for f in fichiers:
            print(" -", f)

    elif choix == "3":
        source = input("❓ Entrez le chemin du fichier à copier : ")
        destination = input("❓ Entrez le dossier de destination : ")
        resultat = copier_fichier_avec_date(source, destination)
        if resultat:
            print(f"✅ Fichier copié dans : {resultat}")

    elif choix == "4":
        dossier = input("❓ Entrez le dossier à utiliser avec la classe : ")
        gestionnaire = GestionnaireFichiers(dossier)

        print("a) Copier un fichier")
        print("b) Compter les fichiers")
        sous_choix = input("❓ Choisissez (a/b) : ")

        if sous_choix == "a":
            fichier = input("❓ Entrez le chemin du fichier à copier : ")
            res = gestionnaire.copier_fichier(fichier)
            if res:
                print(f"✅ Fichier copié dans : {res}")
        elif sous_choix == "b":
            count = gestionnaire.compter_fichiers()
            print(f"✅ Il y a {count} fichiers dans le dossier.")
        else:
            print("❌ Option invalide.")

    elif choix == "5":
        fichier = input("❓ Entrez le nom du fichier de sortie JSON : ")
        exporter_infos_systeme_json(fichier)
        print(f"✅ Infos système exportées dans {fichier}")

    elif choix == "6":
        fichier = input("❓ Entrez le nom du fichier de sortie JSON : ")
        exporter_processus_json(fichier)
        print(f"✅ Processus exportés dans {fichier}")

    elif choix == "7":
        print("✅ Voici les processus qui utilisent plus de 2% de RAM :")
        afficher_gros_processus_seulement()

    elif choix == "8":
        try:
            chemin = input("❓ Chemin vers le fichier (csv/json/xlsx) à analyser : ")
            df = lire_fichier_dynamique(chemin)

            df_yes = filtrer_boolean_yes(df)
            df_reddit = filtrer_url_reddit(df)

            p1, p2 = pourcentage_conditions(df, df_yes, df_reddit)
            print(f"✅ Lignes avec boolean == 'Yes' : {p1:.2f}%")
            print(f"✅ Lignes avec url contenant 'reddit' : {p2:.2f}%")

            exporter_df(df_yes, "./data/exports/filtre_boolean_yes.csv")
            exporter_df(df_reddit, "./data/exports/filtre_url_reddit.csv")
            print("✅ Deux fichiers exportés : `filtre_boolean_yes.csv` et `filtre_url_reddit.csv`")
        except Exception as e:
            print(f"❌ Erreur : {e}")

    elif choix == "9":
        lister_interfaces_reseau_local()

    elif choix == "10":
        host = input("❓ Adresse IP/nom d’hôte de la machine distante : ")
        user = input("❓ Nom d’utilisateur : ")
        password = input("🔐 Mot de passe SSH : ")
        lister_interfaces_reseau_distant(host, user, password)

    elif choix == "0":
        print("Au revoir ! 👋")
        break

    else:
        print("❌ Option invalide, réessayez.")
