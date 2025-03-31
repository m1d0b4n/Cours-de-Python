import os
import requests
import csv
import json
from dotenv import load_dotenv

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()

# Récupérer la clé API Numverify depuis le fichier .env
NUMVERIFY_API_KEY = os.getenv("NUMVERIFY_API_KEY")
if not NUMVERIFY_API_KEY:
    print("Erreur : la clé API Numverify n'est pas définie dans le fichier .env")
    exit(1)

def get_numverify_data(phone_number):
    """
    Envoie une requête GET à l'API Numverify pour un numéro de téléphone donné.
    Retourne les données sous forme de dictionnaire.
    Gère le cas où l'API retourne un code 4xx.
    """
    url = "http://apilayer.net/api/validate"
    params = {
        "access_key": NUMVERIFY_API_KEY,
        "number": phone_number,
        # Vous pouvez ajouter "country_code" ou "format" si besoin, selon la documentation.
    }
    try:
        response = requests.get(url, params=params)
        if 400 <= response.status_code < 500:
            print(f"Erreur lors de la requête Numverify (code {response.status_code}): {response.text}")
            return {}
        # On vérifie que la réponse n'est pas vide et qu'elle est bien au format JSON
        if response.text.strip() == "":
            print("La réponse de l'API est vide.")
            return {}
        return response.json()
    except Exception as e:
        print("Exception lors de la requête à Numverify:", e)
        return {}

def save_numverify_data_csv(data, filename):
    """
    Sauvegarde le dictionnaire 'data' dans un fichier CSV dans le dossier ./data/.
    Chaque ligne du CSV contiendra une clé et sa valeur associée.
    """
    os.makedirs("data", exist_ok=True)
    file_path = os.path.join("data", filename)
    try:
        with open(file_path, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Clé", "Valeur"])
            for key, value in data.items():
                writer.writerow([key, value])
        print("Données Numverify sauvegardées dans", file_path)
    except Exception as e:
        print("Erreur lors de la sauvegarde en CSV:", e)

def file_to_dict(file_path):
    """
    Lit un fichier texte et stocke son contenu dans un dictionnaire 
    où chaque clé est le numéro de la ligne et la valeur le contenu de la ligne.
    """
    result = {}
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            for i, line in enumerate(f, start=1):
                result[i] = line.rstrip("\n")
        return result
    except Exception as e:
        print("Erreur lors de la lecture du fichier:", e)
        return {}

def export_to_json(data, filename):
    """
    Exporte le dictionnaire 'data' dans un fichier JSON dans le dossier ./data/.
    """
    os.makedirs("data", exist_ok=True)
    file_path = os.path.join("data", filename)
    try:
        with open(file_path, "w", encoding="utf-8") as jsonfile:
            json.dump(data, jsonfile, indent=4)
        print("Données exportées en JSON dans", file_path)
    except Exception as e:
        print("Erreur lors de l'export en JSON:", e)

def export_file_dict_csv(data, filename):
    """
    Exporte le dictionnaire 'data' (où chaque clé représente le numéro d'une ligne et la valeur le contenu)
    dans un fichier CSV dans le dossier ./data/ avec des colonnes : Ligne, Contenu et Nombre de Caractères.
    """
    os.makedirs("data", exist_ok=True)
    file_path = os.path.join("data", filename)
    try:
        with open(file_path, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Ligne", "Contenu", "Nombre de Caractères"])
            for line_num, content in data.items():
                writer.writerow([line_num, content, len(content)])
        print("Données exportées en CSV dans", file_path)
    except Exception as e:
        print("Erreur lors de l'export en CSV:", e)

def main():
    # Exercice 3, Question 1 : Requête à l'API Numverify
    print("=== Exercice 3, Question 1 : Requête à l'API Numverify ===")
    phone_number = input("Entrez un numéro de téléphone à rechercher avec Numverify : ")
    numverify_data = get_numverify_data(phone_number)
    print("Données reçues de Numverify :", numverify_data)
    
    # Exercice 3, Question 2 : Sauvegarder les données Numverify dans un CSV
    print("\n=== Exercice 3, Question 2 : Sauvegarder les données Numverify dans un CSV ===")
    save_numverify_data_csv(numverify_data, "numverify_data.csv")
    
    # Exercice 3, Question 3 : Exporter le contenu d'un fichier texte en JSON
    print("\n=== Exercice 3, Question 3 : Exporter le contenu d'un fichier texte en JSON ===")
    file_path = input("Entrez le chemin d'un fichier texte pour l'export en JSON : ")
    file_data = file_to_dict(file_path)
    export_to_json(file_data, "file_content.json")
    
    # Exercice 3, Question 4 : Exporter le contenu d'un fichier texte en CSV avec colonnes
    print("\n=== Exercice 3, Question 4 : Exporter le contenu d'un fichier texte en CSV avec colonnes ===")
    export_file_dict_csv(file_data, "file_content.csv")

if __name__ == "__main__":
    main()
