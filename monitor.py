import urllib.request
import datetime
import time

URL = "https://paruluniversity.ac.in/"

def check_site():
    # Start the stopwatch
    start_time = time.time()
    try:
        code = urllib.request.urlopen(URL, timeout=10).getcode()
        # Stop the stopwatch and convert to milliseconds
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
    
    # Notice the new Latency added to the log!
    log_entry = f"{timestamp} | {URL} | Status: {status} | Latency: {latency}ms\n"
    
    with open("status_log.txt", "a") as file:
        file.write(log_entry)
        
    print(f"Mission accomplished. Logged: {log_entry}")
