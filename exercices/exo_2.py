import ipaddress

# Fonctions de validation d'IP (adaptées de l'exercice 1)
def check_ipv4(ip):
    try:
        ipaddress.IPv4Address(ip)
        return True
    except:
        return False

def check_ipv6(ip):
    try:
        ipaddress.IPv6Address(ip)
        return True
    except:
        return False

# Q1 : Traitement d'un dictionnaire host:ip avec gestion d'erreur (try-except)
def process_ip_dict_try():
    print("Exercice 2, Q1 : Traitement d'un dictionnaire host:ip avec try-except")
    input_str = input("Entrez des paires host:ip séparées par un espace (ex: host1:192.168.1.1 host2:fe80::1): ")
    pairs = input_str.split()
    for pair in pairs:
        try:
            # On attend que chaque paire contienne un ':' pour séparer host et ip
            host, ip = pair.split(":", 1)
            # Simulation d'erreur : si le host est "erreur", on lève volontairement une exception
            if host.lower() == "erreur":
                raise ValueError("Erreur simulée pour le host 'erreur'")
            if check_ipv4(ip):
                print(f"{host} -> Adresse IPv4")
            elif check_ipv6(ip):
                print(f"{host} -> Adresse IPv6")
            else:
                print(f"{host} -> Adresse IP invalide")
        except Exception as e:
            print(f"Erreur lors du traitement de la paire '{pair}': {e}")

# Q2 : Méthode qui remplace certaines lettres par "x" dans un fichier texte.
def replace_letters_in_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        # Ici, on remplace toutes les voyelles (majuscule et minuscule) par "x"
        for letter in "aeiouAEIOU":
            content = content.replace(letter, "x")
        # Enregistrer le contenu modifié dans un nouveau fichier pour ne pas écraser l'original
        new_file = "modified_" + file_path
        with open(new_file, "w", encoding="utf-8") as f:
            f.write(content)
        print("Le contenu modifié a été enregistré dans", new_file)
    except Exception as e:
        print("Erreur lors de la modification du fichier :", e)

# Q3 : Stocker le contenu d'un fichier texte dans un dictionnaire {1: "ligne 1", 2: "ligne 2", ...}
def file_to_dict(file_path):
    result = {}
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            for i, line in enumerate(f, start=1):
                result[i] = line.rstrip("\n")
        return result
    except Exception as e:
        print("Erreur lors de la lecture du fichier :", e)
        return {}

# Q4 : Afficher proprement chaque élément du dictionnaire
def print_file_dict(file_dict):
    for num, line in file_dict.items():
        print(f"Ligne numéro {num} : {len(line)} caractères → \"{line}\"")

def main():
    # Q1 : Traitement d'un dictionnaire host:ip avec try-except et simulation d'erreur
    process_ip_dict_try()

    # Q2 : Remplacement de lettres dans un fichier texte
    print("\nExercice 2, Q2 : Remplacer certaines lettres par 'x' dans un fichier texte")
    file_path = input("Entrez le chemin du fichier texte à modifier : ")
    replace_letters_in_file(file_path)

    # Q3 : Stocker le contenu d'un fichier texte dans un dictionnaire
    print("\nExercice 2, Q3 : Stocker le contenu d'un fichier dans un dictionnaire")
    file_path2 = input("Entrez le chemin du fichier texte à lire : ")
    file_dict = file_to_dict(file_path2)
    print("Contenu stocké dans le dictionnaire :", file_dict)

    # Q4 : Affichage formaté du contenu du dictionnaire
    print("\nExercice 2, Q4 : Affichage formaté du contenu du dictionnaire")
    print_file_dict(file_dict)

main()
