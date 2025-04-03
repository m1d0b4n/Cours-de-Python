import psutil

# --- Q1 : Interfaces réseau locales via psutil (cross-platform) ---
def lister_interfaces_reseau_local():
    print("✅ Interfaces réseau détectées (via psutil) :\n")
    interfaces = psutil.net_if_addrs()

    for nom_interface, adresses in interfaces.items():
        print(f"🔸 Interface : {nom_interface}")
        for addr in adresses:
            famille = addr.family.name if hasattr(addr.family, "name") else str(addr.family)
            if famille == "AF_INET":
                type_ip = "IPv4"
            elif famille == "AF_INET6":
                type_ip = "IPv6"
            elif famille == "AF_PACKET" or "MAC" in famille:
                type_ip = "MAC"
            else:
                type_ip = famille
            print(f"   - {type_ip} : {addr.address}")
        print()

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
