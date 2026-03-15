# serverless-heartbeat
A serverless CI/CD pipeline built with Python and GitHub Actions to automate website uptime monitoring.


<div align="center">

# 🫀 Enterprise-Grade Serverless Heartbeat
**Automated Uptime Monitoring | Real-time Alerting | Latency Analytics**

![Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python)
![GitHub Actions](https://img.shields.io/badge/CI/CD-GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions)
![Discord](https://img.shields.io/badge/Alerts-Discord_Webhook-5865F2?style=for-the-badge&logo=discord)
![Uptime Status](https://github.com/maiiapiyushhoon/serverless-heartbeat/actions/workflows/heartbeat.yml/badge.svg)

[🚀 View Live Dashboard](https://maiiapiyushhoon.github.io/serverless-heartbeat/)

</div>

---

## 📖 Project Overview
This is a production-ready, zero-cost monitoring solution. Instead of paying for uptime services, this project utilizes **Infrastructure as Code (IaC)** principles to turn a GitHub repository into a living compute engine. It monitors target web infrastructure, tracks performance degradation, and alerts stakeholders via Discord.

## 🛠️ Technical Stack & Tools

| Component | Tool / Tech | Purpose |
| :--- | :--- | :--- |
| **Engine** | Python 3.10 | Core logic, Latency math, & HTML generation |
| **Orchestrator** | GitHub Actions | Serverless execution & Cron scheduling |
| **Security** | GitHub Secrets | Encrypted storage for Discord Webhooks |
| **Alerting** | Discord API | Instant Incident Response notifications |
| **Hosting** | GitHub Pages | Live GitOps status dashboard |
| **Database** | Flat-file (TXT) | Persistent state management via Git commits |

---

## 🏗️ System Architecture

1. **The Probe (Latency Tracking):** The Python script doesn't just check for `200 OK`. It uses a high-precision stopwatch to measure the response time in milliseconds. This allows for detecting "Slow-Downs" before they become "Shut-Downs."

2. **The Incident Response (Discord Integration):** Using `os.getenv`, the script securely retrieves a Discord Webhook. If the site is down or latency exceeds **1000ms**, the bot fires an emergency alert with a full diagnostic report.

3. **The GitOps Pipeline (Automation):** The `.github/workflows/heartbeat.yml` handles the dirty
4. 
