# serverless-heartbeat
A serverless CI/CD pipeline built with Python and GitHub Actions to automate website uptime monitoring.


<div align="center">

# 🫀 Serverless Heartbeat Monitor

![Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python)
![GitHub Actions](https://img.shields.io/badge/Automated_by-GitHub_Actions-2088FF?style=for-the-badge&logo=github-actions)
![Zero Cost](https://img.shields.io/badge/Infrastructure-Zero_Cost-success?style=for-the-badge)
![Uptime Status](https://github.com/maiiapiyushhoon/serverless-heartbeat/actions/workflows/heartbeat.yml/badge.svg)

*A lightweight, serverless CI/CD uptime monitoring system.*

</div>

---

## 🚀 Overview

Instead of relying on heavy servers or paid third-party tools to monitor website uptime, this project leverages **Infrastructure as Code (IaC)** and automated pipelines to create a self-sustaining monitoring loop entirely in the cloud.

## 📊 Monitored Endpoints

| Target Website | Infrastructure Type | Expected HTTP | Ping Frequency |
|----------------|---------------------|---------------|----------------|
| [Parul University](https://paruluniversity.ac.in) | Web Portal | `200 OK` | Every 6 Hours |
| *Your Site Here* | *Web / API* | `200 OK` | *Customizable* |

## 🏗️ Architecture & Flow

This project demonstrates a modern serverless workflow:
1. **The Probe:** A Python script (`monitor.py`) pings the target URL and evaluates response codes.
2. **The Automator:** A GitHub Actions workflow (`heartbeat.yml`) acts as the cron scheduler, spinning up an ephemeral runner.
3. **The CI/CD Loop:** The bot automatically commits and pushes the updated log back to the repository state.

<details>
<summary><b>🛠️ Click here to see How to Fork & Use</b></summary>
<br>
Want to monitor your own site? 

1. Fork this repository to your account.
2. Open `monitor.py` and update the `URL` variable to your target website.
3. Go to the **Actions** tab and enable workflows.
4. The GitHub Action will automatically begin monitoring your site every 6 hours!
</details>

---
*Built to demonstrate applied DevOps, CI/CD automation, and cloud-native thinking.*
