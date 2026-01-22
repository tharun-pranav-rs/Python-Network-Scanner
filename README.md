# 🕵️ Active Network Vulnerability Scanner

A Python-based automated security auditing tool that actively probes network infrastructure to detect unauthorized exposed services (Open Ports). Integrated with **Discord Webhooks** for real-time SOC alerting.

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white)
![Security](https://img.shields.io/badge/Security-Network%20Auditing-red)
![Docker](https://img.shields.io/badge/Docker-Supported-blue?logo=docker&logoColor=white)

<br>

📸 Demo

<img width="443" height="184" alt="Screenshot 2026-01-22 125108" src="https://github.com/user-attachments/assets/79380132-4303-471b-a8ad-1789e5716032" />

<img width="456" height="184" alt="Screenshot 2026-01-22 125141" src="https://github.com/user-attachments/assets/ed184aaf-6ad4-4c3b-94fd-d5db24c56a77" />

<img width="607" height="285" alt="Screenshot 2026-01-22 204100" src="https://github.com/user-attachments/assets/7d41ae0a-a792-4113-be85-091ef07697d0" />


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
### 2. Run the Scanner
docker run -e TARGET_IP="host.docker.internal" --add-host=host.docker.internal:host-gateway vuln-scanner

🛠️ Manual Usage
1. Clone the Repository
git clone [https://github.com/tharun-pranav-rs/Python-Network-Scanner.git](https://github.com/tharun-pranav-rs/Python-Network-Scanner.git)
cd Python-Network-Scanner
2. Install Dependencies
pip install -r requirements.txt
3. Configure & Run
Open Scanner.py and paste your Discord Webhook URL.

Set the TARGET_IP (Default is 127.0.0.1).

Run the auditor:
python Scanner.py

🛡️ Disclaimer
This tool is intended for defensive security purposes only. Ensure you have authorization before scanning any network.
