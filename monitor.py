import urllib.request
import json
import os
import datetime
import time

URL = "https://paruluniversity.ac.in/"
# Pulls the secret from GitHub's vault securely!
WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK") 

def send_discord_alert(message):
    if not WEBHOOK_URL:
        print("❌ ERROR: Discord Webhook secret is empty or missing!")
        return
    
    print("✅ Secret found! Attempting to ping Discord...")
    data = {"content": message}
    
    # The Disguise: Tells Discord we are a normal web browser
    headers = {
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
    
    req = urllib.request.Request(WEBHOOK_URL, json.dumps(data).encode(), headers)
    try:
        urllib.request.urlopen(req)
        print("✅ Discord message sent successfully!")
    except Exception as e:
        print(f"❌ Discord blocked it! Reason: {e}")

def check_site():
    start_time = time.time()
    try:
        code = urllib.request.urlopen(URL, timeout=10).getcode()
        latency = round((time.time() - start_time) * 1000) 
        
        if code == 200:
            return "🟢 UP", latency
        else:
            return f"🟡 WARNING ({code})", latency
    except Exception as e:
        return "🔴 DOWN", 0

if __name__ == "__main__":
    status, latency = check_site()
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    log_entry = f"{timestamp} | {URL} | Status: {status} | Latency: {latency}ms\n"
    
    with open("status_log.txt", "a") as file:
        file.write(log_entry)
        
    print(f"Logged: {log_entry}")

    # The Alert Trigger: Only ping Discord if it's down, warning, or dangerously slow (> 1000ms)
    if "DOWN" in status or "WARNING" in status or latency > 1000:
        alert_msg = f"🚨 **MONITOR ALARM** 🚨\n**Target:** {URL}\n**Status:** {status}\n**Latency:** {latency}ms"
        send_discord_alert(alert_msg)
