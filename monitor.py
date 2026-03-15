import urllib.request, json, os, datetime, time

URL = "https://paruluniversity.ac.in/"
WEBHOOK_URL = os.getenv("DISCORD_WEBHOOK") 

def send_discord_alert(message):
    if not WEBHOOK_URL: return
    data = {"content": message}
    headers = {"Content-Type": "application/json", "User-Agent": "Mozilla/5.0"}
    req = urllib.request.Request(WEBHOOK_URL, json.dumps(data).encode(), headers)
    try: urllib.request.urlopen(req)
    except Exception as e: print(f"Alert failed: {e}")

def check_site():
    start_time = time.time()
    try:
        code = urllib.request.urlopen(URL, timeout=10).getcode()
        latency = round((time.time() - start_time) * 1000) 
        return ("🟢 UP", latency) if code == 200 else (f"🟡 WARNING ({code})", latency)
    except: return ("🔴 DOWN", 0)

def generate_html_dashboard():
    try:
        with open("status_log.txt", "r") as f: logs = f.readlines()[-10:]
    except: logs = ["No data yet."]
    html_content = f"""<!DOCTYPE html><html><head><title>Status</title><style>body{{background:#0d1117;color:#c9d1d9;font-family:monospace;padding:20px;text-align:center;}}.box{{background:#161b22;padding:20px;border-radius:10px;border:1px solid #30363d;display:inline-block;text-align:left;}}</style></head><body><h1>🫀 Status Dashboard</h1><p>Monitoring: {URL}</p><div class="box">{"<br>".join(logs)}</div></body></html>"""
    with open("index.html", "w") as f: f.write(html_content)

if __name__ == "__main__":
    status, latency = check_site()
    log_entry = f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')} | {status} | {latency}ms\n"
    with open("status_log.txt", "a") as f: f.write(log_entry)
    if "DOWN" in status or latency > 1000:
        send_discord_alert(f"🚨 **ALARM**\n**Status:** {status}\n**Latency:** {latency}ms")
    generate_html_dashboard()
    
