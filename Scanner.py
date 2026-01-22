import requests
import json
import datetime
import time
import socket

# ---------------- CONFIGURATION ---------------- #
# 1. PASTE YOUR WEBHOOK URL HERE
WEBHOOK_URL = "YOUR WEBHOOK URL"

# 2. Target IP (Localhost)
TARGET_IP = "127.0.0.1" 

# 3. Ports to scan
PORTS_TO_SCAN = [21, 22, 80, 445, 3306, 8000]

# ---------------- THE ALERT FUNCTION ---------------- #
def send_security_alert(title, description, severity="INFO", port="N/A"):
    colors = {
        "INFO": 3447003,      # Blue
        "WARNING": 16776960,  # Yellow
        "CRITICAL": 15158332  # Red
    }
    
    # FIXED: Updated timestamp format to remove warning
    timestamp = datetime.datetime.now(datetime.timezone.utc).isoformat()
    
    payload = {
        "username": "Vulnerability Scanner",
        "avatar_url": "https://i.imgur.com/4M34hi2.png",
        "embeds": [{
            "title": f"🚨 {title}",
            "description": description,
            "color": colors.get(severity, 3447003),
            "timestamp": timestamp,
            "fields": [
                {"name": "Target IP", "value": f"`{TARGET_IP}`", "inline": True},
                {"name": "Port", "value": f"**{port}**", "inline": True}
            ]
        }]
    }

    try:
        response = requests.post(WEBHOOK_URL, data=json.dumps(payload), headers={"Content-Type": "application/json"})
        # ADDED: Feedback so you know it worked
        if response.status_code == 204:
            print("  ✅ Alert sent to Discord!")
        else:
            print(f"  ❌ Failed to send alert: {response.status_code}")
    except Exception as e:
        print(f"  ❌ Error: {e}")

# ---------------- THE PORT SCANNER ---------------- #
def check_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5) # Faster timeout
        result = sock.connect_ex((ip, port))
        sock.close()
        return result == 0
    except:
        return False

# ---------------- MAIN LOOP ---------------- #
print(f"🛡️ vulnerability_scanner.py started on {TARGET_IP}...")
print("Press Ctrl+C to stop.")

while True:
    print(f"\n🔍 Scanning {TARGET_IP}...")
    
    for port in PORTS_TO_SCAN:
        print(f"  > Checking Port {port}...", end="")
        
        if check_port(TARGET_IP, port):
            print(f" OPEN! 🚨")
            
            # Determine Severity
            severity = "INFO"
            if port in [21, 22, 445, 3306]:
                severity = "CRITICAL"
                
            send_security_alert(
                title="Open Port Detected",
                description=f"Port **{port}** is exposed. Check firewall rules immediately.",
                severity=severity,
                port=port
            )
        else:
            print(" Closed.")
            
    print("Scan complete. Sleeping for 60 seconds...")
    time.sleep(60)
