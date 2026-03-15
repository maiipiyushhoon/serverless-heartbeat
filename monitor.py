import urllib.request
import datetime

URL = "https://paruluniversity.ac.in/"

def check_site():
    try:
        # Pings the website to see if it responds
        code = urllib.request.urlopen(URL, timeout=10).getcode()
        if code == 200:
            return "🟢 UP"
        else:
            return f"🟡 WARNING ({code})"
    except Exception as e:
        return "🔴 DOWN"

if __name__ == "__main__":
    status = check_site()
    # Gets the current time
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Formats the log message
    log_entry = f"{timestamp} | {URL} | Status: {status}\n"
    
    # Opens the log file and appends the new entry at the bottom
    with open("status_log.txt", "a") as file:
        file.write(log_entry)
        
    print(f"Mission accomplished. Logged: {log_entry}")
  
