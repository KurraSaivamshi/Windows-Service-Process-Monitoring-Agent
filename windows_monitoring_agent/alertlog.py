
import csv
import os
from datetime import datetime

# CSV file for centralized security alerts
ALERT_LOG_FILE = "security_alerts.csv"

# CSV column names
CSV_FIELDS = [
    "Timestamp",
    "Module",
    "Alert Type",
    "Severity",
    "Details"
]


def log_alert(module, alert_type, severity, details):
    """Save a security alert to the CSV file."""

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    file_exists = os.path.exists(ALERT_LOG_FILE)

    try:
        with open(
            ALERT_LOG_FILE,
            "a",
            newline="",
            encoding="utf-8"
        ) as file:

            writer = csv.DictWriter(
                file,
                fieldnames=CSV_FIELDS
            )

            # Write header if the file is new
            if not file_exists:
                writer.writeheader()

            # Write alert information
            writer.writerow({
                "Timestamp": timestamp,
                "Module": module,
                "Alert Type": alert_type,
                "Severity": severity,
                "Details": details
            })

        print("\n[ALERT LOGGED]")
        print(f"Module: {module}")
        print(f"Alert Type: {alert_type}")
        print(f"Severity: {severity}")
        print(f"Details: {details}")

    except Exception as error:
        print(f"Error logging alert: {error}")


def view_alerts():
    """Display all saved security alerts."""

    if not os.path.exists(ALERT_LOG_FILE):
        print("No security alerts have been logged yet.")
        return

    print("\n" + "=" * 70)
    print(" CENTRALIZED SECURITY ALERT LOG")
    print("=" * 70)

    with open(
        ALERT_LOG_FILE,
        "r",
        newline="",
        encoding="utf-8"
    ) as file:

        reader = csv.DictReader(file)

        total_alerts = 0

        for row in reader:

            print("-" * 70)
            print(f"Timestamp: {row['Timestamp']}")
            print(f"Module: {row['Module']}")
            print(f"Alert Type: {row['Alert Type']}")
            print(f"Severity: {row['Severity']}")
            print(f"Details: {row['Details']}")

            total_alerts += 1

    print("\n" + "=" * 70)
    print(f"Total Logged Alerts: {total_alerts}")
    print("=" * 70)


if __name__ == "__main__":

    # Test alert logging
    log_alert(
        module="Process Analyzer",
        alert_type="Suspicious Parent-Child Process",
        severity="HIGH",
        details="PowerShell was launched by an unexpected parent process."
    )

    log_alert(
        module="Security Event Monitor",
        alert_type="Credential Manager Access",
        severity="MEDIUM",
        details="Windows Event ID 5379 was detected."
    )

    # Display saved alerts
    view_alerts()
