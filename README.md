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
## 📸 Demo

![Screenshot 1](https://github.com/user-attachments/assets/5d0bba90-8532-480f-a062-9666c6893786)

<br>

![Screenshot 2](https://github.com/user-attachments/assets/9d1840c5-1980-4d15-a8d6-cdf36c01ecc5)

<br>

### 🛡️ Disclaimer
**This tool is intended for defensive security purposes only. Ensure you have authorization before scanning any network.**
