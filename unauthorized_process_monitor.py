
import psutil
from datetime import datetime
import os
import csv

# Suspicious locations to monitor
SUSPICIOUS_LOCATIONS = [
    "\\temp\\",
    "\\appdata\\local\\temp\\",
    "\\downloads\\"
]


def monitor_processes():
    alerts = []

    print("\n" + "=" * 70)
    print(" UNAUTHORIZED PROCESS MONITOR")
    print("=" * 70)

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

                    alert = {
                        "Timestamp": datetime.now().strftime(
                            "%Y-%m-%d %H:%M:%S"
                        ),
                        "Process_Name": process_name,
                        "PID": process_id,
                        "Username": username,
                        "Executable_Path": executable_path,
                        "Severity": "HIGH",
                        "Alert": "Process Running from Suspicious Location"
                    }

                    alerts.append(alert)
                    break

        except (
            psutil.NoSuchProcess,
            psutil.AccessDenied,
            psutil.ZombieProcess
        ):
            continue

    return alerts


def display_alerts(alerts):
    print("\n" + "=" * 70)
    print(" PROCESS SECURITY ALERTS")
    print("=" * 70)

    if not alerts:
        print("No suspicious processes detected.")

    else:
        for alert in alerts:
            print("\n[", alert["Severity"], "]")
            print("Process Name:", alert["Process_Name"])
            print("PID:", alert["PID"])
            print("Username:", alert["Username"])
            print("Executable Path:", alert["Executable_Path"])
            print("Alert:", alert["Alert"])
            print("Timestamp:", alert["Timestamp"])

    print("\nTotal Alerts:", len(alerts))


def save_alerts_to_csv(alerts):
    if not alerts:
        print("\nNo alerts to save.")
        return

    filename = "unauthorized_process_alerts.csv"

    file_exists = os.path.isfile(filename)

    with open(filename, "a", newline="", encoding="utf-8") as file:
        fieldnames = [
            "Timestamp",
            "Process_Name",
            "PID",
            "Username",
            "Executable_Path",
            "Severity",
            "Alert"
        ]

        writer = csv.DictWriter(
            file,
            fieldnames=fieldnames
        )

        if not file_exists:
            writer.writeheader()

        writer.writerows(alerts)

    print("\nAlerts saved to:", filename)


if __name__ == "__main__":
    process_alerts = monitor_processes()

    display_alerts(process_alerts)

    save_alerts_to_csv(process_alerts)
