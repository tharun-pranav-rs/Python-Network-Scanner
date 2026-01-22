# 🕵️ Active Network Vulnerability Scanner

A Python-based automated security auditing tool that actively probes network infrastructure to detect unauthorized exposed services (Open Ports). Integrated with **Discord Webhooks** for real-time SOC alerting.

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python&logoColor=white)
![Security](https://img.shields.io/badge/Security-Network%20Auditing-red)

<br>

## ⚡ Key Capabilities

* **Active Port Scanning:** Utilizes raw TCP Sockets to perform "Connect" scans on target infrastructure.
* **Risk Classification:** Automatically categorizes ports (e.g., Port 445 vs Port 80) and assigns severity levels (INFO vs CRITICAL).
* **Real-time Incident Response:** Pushes JSON payloads to Discord for immediate notification.
* **IPv4/IPv6 Logic:** Handles local binding to detect services running on specific interfaces.

<br>

## 🛠️ Usage

### 1. Clone the Repository
```bash
git clone [https://github.com/tharun-pranav-rs/Python-Network-Scanner.git](https://github.com/tharun-pranav-rs/Python-Network-Scanner.git)
cd Python-Network-Scanner
2. Install Dependencies
Bash

pip install -r requirements.txt
3. Configure & Run
Open Scanner.py and paste your Discord Webhook URL.

Set the TARGET_IP (Default is 127.0.0.1).

Run the auditor:


python Scanner.py
📸 Demo

<img width="443" height="184" alt="Screenshot 2026-01-22 125108" src="https://github.com/user-attachments/assets/245a7c4b-650b-49f8-ab11-5f63bc2d99e3" />




<img width="456" height="184" alt="Screenshot 2026-01-22 125141" src="https://github.com/user-attachments/assets/befdddba-66fd-4921-ad0c-644adcc6bae6" />





🛡️ Disclaimer
This tool is intended for defensive security purposes only. Ensure you have authorization before scanning any network.
