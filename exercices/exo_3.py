import os
import requests
import csv
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
    }
    try:
        response = requests.get(url, params=params)
        if 400 <= response.status_code < 500:
            print(f"Erreur lors de la requête Numverify (code {response.status_code}): {response.text}")
            return {}
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

def main():
    # Exercice 3, Question 1 : Requête à l'API Numverify
    print("=== Exercice 3, Question 1 : Requête à l'API Numverify ===")
    phone_number = input("Entrez un numéro de téléphone à rechercher avec Numverify : ")
    numverify_data = get_numverify_data(phone_number)
    print("Données reçues de Numverify :", numverify_data)
    
    # Exercice 3, Question 2 : Sauvegarder les données Numverify dans un CSV
    print("\n=== Exercice 3, Question 2 : Sauvegarder les données Numverify dans un CSV ===")
    save_numverify_data_csv(numverify_data, "numverify_data.csv")

if __name__ == "__main__":
    main()
