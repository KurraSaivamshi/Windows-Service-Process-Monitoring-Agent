
import psutil
import time
import csv
import os
from datetime import datetime


# Scan interval in seconds
SCAN_INTERVAL = 10

# Suspicious process locations
SUSPICIOUS_LOCATIONS = [
    "\\temp\\",
    "\\appdata\\local\\temp\\",
    "\\downloads\\"
]

# CSV log file
LOG_FILE = "continuous_monitor_alerts.csv"

# Store already detected processes
detected_processes = set()


def scan_processes():

    for process in psutil.process_iter(
        ["pid", "name", "exe", "username"]
    ):

        try:
            process_info = process.info

            process_name = process_info.get("name")
            process_id = process_info.get("pid")
            executable_path = process_info.get("exe")
            username = process_info.get("username")

            if not executable_path:
                continue

            normalized_path = executable_path.lower()

            for location in SUSPICIOUS_LOCATIONS:

                if location in normalized_path:

                    process_key = (process_id, executable_path)

                    # Avoid repeating the same alert
                    if process_key in detected_processes:
                        break

                    detected_processes.add(process_key)

                    timestamp = datetime.now().strftime(
                        "%Y-%m-%d %H:%M:%S"
                    )

                    print("\n" + "=" * 60)
                    print(" SECURITY ALERT DETECTED")
                    print("=" * 60)

                    print("Process Name:", process_name)
                    print("Process ID:", process_id)
                    print("Username:", username)
                    print("Executable Path:", executable_path)
                    print("Severity: HIGH")
                    print("Timestamp:", timestamp)

                    save_alert(
                        timestamp,
                        process_name,
                        process_id,
                        username,
                        executable_path
                    )

                    break

        except (
            psutil.NoSuchProcess,
            psutil.AccessDenied,
            psutil.ZombieProcess
        ):
            continue


def save_alert(
    timestamp,
    process_name,
    process_id,
    username,
    executable_path
):

    file_exists = os.path.isfile(LOG_FILE)

    with open(LOG_FILE, "a", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        if not file_exists:
            writer.writerow([
                "Timestamp",
                "Process_Name",
                "PID",
                "Username",
                "Executable_Path",
                "Severity"
            ])

        writer.writerow([
            timestamp,
            process_name,
            process_id,
            username,
            executable_path,
            "HIGH"
        ])


def main():

    print("=" * 60)
    print(" CONTINUOUS PROCESS MONITORING AGENT")
    print("=" * 60)

    print("Monitoring Interval:", SCAN_INTERVAL, "seconds")
    print("Monitoring Started...")
    print("Press CTRL + C to stop monitoring.")

    try:

        while True:

            scan_processes()

            print(
                "\nNext scan in",
                SCAN_INTERVAL,
                "seconds..."
            )

            time.sleep(SCAN_INTERVAL)

    except KeyboardInterrupt:

        print("\nMonitoring stopped by user.")

        print("Total Unique Alerts:", len(detected_processes))


if __name__ == "__main__":
    main()
