import os
import getmac
import socket
import getpass
import requests
import platform

def extract():
    # Get Hostname
    hostname = socket.gethostname()

    # Get Current User
    current_user = getpass.getuser()

    # Get OS Information
    os_system = platform.system()  # e.g., Windows, Linux, Darwin (macOS)
    os_version = platform.version()  # OS version

    # Get Local IP Address
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
                s.connect(("8.8.8.8", 80))  # Connect to a public DNS server
                local_ip = s.getsockname()[0]
    except Exception as e:
        local_ip = "Unavailable"

    # Get Public IP Address
    try:
        public_ip = requests.get("https://api.ipify.org").text
    except Exception as e:
        public_ip = "Unavailable"
        
    # Get MAC Address
    mac = getmac.get_mac_address()

    info = {
        "Hostname": hostname,
        "User": current_user,
        "OS": os_system,
        "OS version": os_version,
        "Mac": mac,
        "Local IP": local_ip,
        "Public IP": public_ip,
    }
    
    return info

if __name__ == '__main__':
    print(extract())
