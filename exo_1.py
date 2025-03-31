import ipaddress

# Fonction simple pour vérifier une adresse IPv4
def check_ipv4(ip):
    try:
        ipaddress.IPv4Address(ip)
        return True
    except:
        return False

# Fonction simple pour vérifier une adresse IPv6
def check_ipv6(ip):
    try:
        ipaddress.IPv6Address(ip)
        return True
    except:
        return False

# Fonction pour détecter et renvoyer la version (4 ou 6) d'une adresse IP
def detect_ip(ip):
    if check_ipv4(ip):
        return 4
    elif check_ipv6(ip):
        return 6
    else:
        return None

def main():
    # Q1 : Demander à l'utilisateur de taper une adresse IPv4 et l'afficher
    ipv4 = input("Tapez une adresse IPv4: ")
    print("Adresse saisie:", ipv4)
    if check_ipv4(ipv4):
        print("L'adresse IPv4 est valide.")
    else:
        print("L'adresse IPv4 est invalide.")

    # Q3 : Demander à l'utilisateur de taper une adresse IPv6 et la vérifier
    ipv6 = input("Tapez une adresse IPv6: ")
    if check_ipv6(ipv6):
        print("L'adresse IPv6 est valide.")
    else:
        print("L'adresse IPv6 est invalide.")

    # Q4 : Détecter si une adresse IP est IPv4 ou IPv6
    ip = input("Tapez une adresse IP (IPv4 ou IPv6): ")
    version = detect_ip(ip)
    if version:
        print("C'est une adresse IPv" + str(version))
    else:
        print("Adresse IP invalide.")

    # Q5 : Traitement d'une liste d'adresses IP (séparées par un espace)
    liste = input("Tapez une liste d'adresses IP séparées par un espace: ")
    liste_ip = liste.split()  # Sépare les adresses par espace
    for ip in liste_ip:
        v = detect_ip(ip)
        if v:
            print(ip, "est une adresse IPv" + str(v))
        else:
            print(ip, "n'est pas valide.")

    # Q6 : Traitement d'un dictionnaire host:ip
    print("Tapez des paires host:ip séparées par un espace (ex: host1:192.168.1.1 host2:fe80::1)")
    paires = input("Votre saisie: ").split()
    for paire in paires:
        # On suppose que chaque paire contient exactement un ':' pour séparer le host et l'adresse IP.
        host, ip = paire.split(":")
        v = detect_ip(ip)
        if v:
            print(host, "-> adresse IPv" + str(v))
        else:
            print(host, "-> adresse invalide")


main()
