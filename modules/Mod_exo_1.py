def is_valid_ipv4(ip):
    try:
        parts = ip.split(".")
        if len(parts) != 4:
            return False
        return all(0 <= int(part) <= 255 for part in parts)
    except ValueError:
        return False

def is_valid_ipv6(ip):
    try:
        parts = ip.split(":")
        if len(parts) != 8:
            return False
        return all(0 <= int(part, 16) <= 0xFFFF for part in parts)
    except ValueError:
        return False

def detect_ip_version(ip):
    if is_valid_ipv4(ip):
        return 4
    elif is_valid_ipv6(ip):
        return 6
    else:
        return 0

def detect_ip_list(ip_list):
    return [(ip, detect_ip_version(ip)) for ip in ip_list]

def detect_ip_dict(ip_dict):
    return {host: detect_ip_version(ip) for host, ip in ip_dict.items()}
