import psutil
import time
import os
from datetime import datetime

# Convert bytes to megabytes
def bytes_to_mb(b):
    return round(b / (1024 ** 2), 2)

# Log file to store memory readings
log_file = "memory_log.txt"

try:
    while True:
        # Clear the terminal screen
        os.system('cls' if os.name == 'nt' else 'clear')

        memory = psutil.virtual_memory()
        total = bytes_to_mb(memory.total)
        used = bytes_to_mb(memory.used)
        available = bytes_to_mb(memory.available)
        percent = memory.percent
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Display memory stats
        print("🧠 Real-Time Memory Monitoring:")
        print("=" * 50)
        print(f"⏰ Time: {now}")
        print(f"📦 Total Memory     : {total} MB")
        print(f"🔴 Used Memory      : {used} MB")
        print(f"🟢 Available Memory : {available} MB")
        print(f"📊 Usage Percent    : {percent} %")

        # Warning if memory usage exceeds 80%
        if percent >= 80:
            print("\033[91m⚠️  Warning: High memory usage!\033[0m")

        print("=" * 50)

        # Save stats to the log file
        with open(log_file, "a") as f:
            f.write(f"{now}, Total: {total} MB, Used: {used} MB, Available: {available} MB, Usage: {percent}%\n")

        time.sleep(1)

except KeyboardInterrupt:
    print("\n❌ Monitoring stopped by user.")
