import socket
import time
import requests
import json
import os

# ---------------- CONFIGURATION ---------------- #
# If running in Docker, this environment variable will override the default
TARGET_IP = os.getenv("TARGET_IP", "127.0.0.1")

# PORTS TO SCAN (Common vulnerable services)
PORTS_TO_SCAN = [21, 22, 80, 445, 3306, 8000, 8080]

# PASTE YOUR DISCORD WEBHOOK URL HERE
WEBHOOK_URL = "YOUR_WEBHOOK"
# ----------------------------------------------- #

def send_discord_alert(port, service_name):
    """Sends a critical alert to Discord."""
    if "YOUR_WEBHOOK_URL" in WEBHOOK_URL:
        print("⚠️ Discord Webhook not configured. Skipping alert.")
        return

    data = {
        "embeds": [{
            "title": "🚨 Open Port Detected!",
            "description": f"Port **{port}** ({service_name}) is exposed on **{TARGET_IP}**.",
            "color": 15548997,  # Red color
            "fields": [
                {"name": "Target IP", "value": TARGET_IP, "inline": True},
                {"name": "Port", "value": str(port), "inline": True},
                {"name": "Action Required", "value": "Check firewall rules immediately."}
            ],
            "footer": {"text": "Python Network Scanner • Security Alert"}
        }]
    }
    try:
        requests.post(WEBHOOK_URL, json=data)
        print(f"   [+] Alert sent to Discord for Port {port}")
    except Exception as e:
        print(f"   [-] Failed to send alert: {e}")

def check_port(ip, port):
    """Tries to connect to a specific port."""
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)  # 1 second timeout
    result = sock.connect_ex((ip, port))
    sock.close()
    return result == 0

def start_scan():
    print(f"\n🔍 Scanning Target: {TARGET_IP}...")
    
    found_open = False
    for port in PORTS_TO_SCAN:
        print(f" > Checking Port {port}...", end="\r")
        if check_port(TARGET_IP, port):
            print(f" > Checking Port {port}... 🔓 OPEN!      ")
            send_discord_alert(port, "Unknown Service")
            found_open = True
        else:
<<<<<<< HEAD
            # Overwrite the line to keep terminal clean
            print(f" > Checking Port {port}... Closed.     ")
    
    if not found_open:
        print("✅ No open ports found.")

if __name__ == "__main__":
    print(f"🛡️ Vulnerability Scanner started...")
    print(f"🎯 Configuration: Scans {TARGET_IP} every 60 seconds.")
    print("Press Ctrl+C to stop.\n")
    
    try:
        while True:
            start_scan()
            print("\nScan complete. Sleeping for 60 seconds...")
            time.sleep(60)
    except KeyboardInterrupt:
        print("\n🛑 Scanner stopped by user.")
=======
            print(" Closed.")
            
    print("Scan complete. Sleeping for 60 seconds...")
    time.sleep(60)
>>>>>>> cbffaa59b918c8195273b2fcc71ac538678c4717
