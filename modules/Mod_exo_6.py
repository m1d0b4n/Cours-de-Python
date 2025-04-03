import json
import platform
import psutil

def exporter_infos_systeme_json(fichier):
    infos = {
        "os": platform.system(),
        "version": platform.version(),
        "architecture": platform.machine(),
        "ram_utilisee": psutil.virtual_memory().used,
        "ram_totale": psutil.virtual_memory().total,
        "cpu": platform.processor()
    }

    with open(fichier, "w") as f:
        json.dump(infos, f, indent=4)

def exporter_processus_json(fichier):
    processus_liste = []

    for proc in psutil.process_iter(attrs=["pid", "name", "cpu_percent", "memory_percent"]):
        try:
            processus_liste.append(proc.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    with open(fichier, "w") as f:
        json.dump(processus_liste, f, indent=4)

def afficher_gros_processus_seulement():
    for proc in psutil.process_iter(attrs=["pid", "name", "memory_percent"]):
        try:
            if proc.info["memory_percent"] > 1.0:
                print(f'{proc.info["name"]} (PID {proc.info["pid"]}) utilise {proc.info["memory_percent"]:.2f}% de RAM')
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
