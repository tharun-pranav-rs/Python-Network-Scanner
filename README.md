# 🕵️ Active Network Vulnerability Scanner

A Python-based automated security auditing tool that actively probes network infrastructure to detect unauthorized exposed services (Open Ports). Integrated with **Discord Webhooks** for real-time SOC alerting.

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white)
![Security](https://img.shields.io/badge/Security-Network%20Auditing-red)
![Docker](https://img.shields.io/badge/Docker-Supported-blue?logo=docker&logoColor=white)

<br>

📸 Demo

![alt text](<Screenshot 2026-01-22 125108.png>)

![alt text](<Screenshot 2026-01-22 125141.png>)

![alt text](<Screenshot 2026-01-22 204100.png>)

## ⚡ Key Capabilities

* **Active Port Scanning:** Utilizes raw TCP Sockets to perform "Connect" scans on target infrastructure.
* **Risk Classification:** Automatically categorizes ports (e.g., Port 445 vs Port 80) and assigns severity levels (INFO vs CRITICAL).
* **Real-time Incident Response:** Pushes JSON payloads to Discord for immediate notification.
* **IPv4/IPv6 Logic:** Handles local binding to detect services running on specific interfaces.

<br>

## 🐳 Docker Usage (Recommended)

Run the scanner in an isolated container without installing Python manually.

### 1. Build the Image
```bash
docker build -t vuln-scanner .
<<<<<<< HEAD

2. Run the Scanner
=======
### 2. Run the Scanner
>>>>>>> 74273a958cc5e485a875dcb1dc3b866dd8f3334a
docker run -e TARGET_IP="host.docker.internal" --add-host=host.docker.internal:host-gateway vuln-scanner

🛠️ Manual Usage
1. Clone the Repository
git clone [https://github.com/tharun-pranav-rs/Python-Network-Scanner.git](https://github.com/tharun-pranav-rs/Python-Network-Scanner.git)
cd Python-Network-Scanner
<<<<<<< HEAD

=======
>>>>>>> 74273a958cc5e485a875dcb1dc3b866dd8f3334a
2. Install Dependencies
pip install -r requirements.txt

3. Configure & Run

Open Scanner.py and paste your Discord Webhook URL.

Set the TARGET_IP (Default is 127.0.0.1).

<<<<<<< HEAD
Run the auditor: python Scanner.py

🛡️ Disclaimer
This tool is intended for defensive security purposes only. Ensure you have authorization before scanning any network.
=======
Run the auditor:
python Scanner.py

🛡️ Disclaimer
This tool is intended for defensive security purposes only. Ensure you have authorization before scanning any network.
>>>>>>> 74273a958cc5e485a875dcb1dc3b866dd8f3334a
