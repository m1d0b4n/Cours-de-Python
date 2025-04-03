import subprocess
import re

# --- Q1 : Interfaces réseau locales via psutil (cross-platform) ---
def lister_interfaces_reseau_local():
    try:
        result = subprocess.run(["ipconfig"], capture_output=True, text=True, encoding="cp850")  # 👈 clé ici
        if result.returncode == 0:
            print("✅ Interfaces détectées (via 'ipconfig' + regex) :\n")

            lignes = result.stdout.splitlines()
            interfaces = []

            for line in lignes:
                match = re.match(r"^Carte (.+?)\s*:$", line.strip())
                if match:
                    nom_interface = match.group(1)
                    interfaces.append(nom_interface)

            if interfaces:
                for i, interface in enumerate(interfaces, 1):
                    print(f"  🔹 {i}. {interface}")
            else:
                print("❌ Aucune interface détectée.")
        else:
            print("❌ Erreur lors de l’exécution de 'ipconfig'.")
    except FileNotFoundError:
        print("❌ La commande 'ipconfig' n’est pas disponible.")
    except Exception as e:
        print(f"❌ Erreur inattendue : {e}")

# --- Q2 : Interfaces réseau distantes via Fabric ---
def lister_interfaces_reseau_distant(host, user, password):
    from fabric import Connection
    try:
        conn = Connection(host=host, user=user, connect_kwargs={"password": password})
        result = conn.run("ip addr", hide=True)
        print("   ")
        print("✅ Interfaces réseau sur la machine distante :\n")
        print(result.stdout)
    except Exception as e:
        print(f"❌ Erreur Fabric : {e}")
