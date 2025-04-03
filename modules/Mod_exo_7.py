import pandas as pd

def lire_fichier_dynamique(chemin_fichier):
    if chemin_fichier.endswith(".csv"):
        return pd.read_csv(chemin_fichier)
    elif chemin_fichier.endswith(".json"):
        return pd.read_json(chemin_fichier)
    elif chemin_fichier.endswith(".xlsx"):
        return pd.read_excel(chemin_fichier)
    else:
        raise ValueError("Format de fichier non pris en charge.")

def filtrer_boolean_yes(df):
    return df[df["boolean"] == "Yes"]

def filtrer_url_reddit(df):
    return df[df["url"].str.contains("reddit", na=False)]

def pourcentage_conditions(df, df_yes, df_reddit):
    total = len(df)
    percent_yes = (len(df_yes) / total) * 100 if total else 0
    percent_reddit = (len(df_reddit) / total) * 100 if total else 0
    return percent_yes, percent_reddit

def exporter_df(df, chemin_sortie):
    df.to_csv(chemin_sortie, index=False)
