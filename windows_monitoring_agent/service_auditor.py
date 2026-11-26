
# FILE: service_auditor.py

import psutil
from datetime import datetime


def audit_services():
    service_list = []
    alerts = []

    for service in psutil.win_service_iter():
        try:
            # Get service details individually to avoid query errors
            service_name = service.name()

            try:
                service_info = service.as_dict()
            except (OSError, psutil.Error):
                continue

            display_name = service_info.get("display_name")
            status = service_info.get("status")
            start_type = service_info.get("start_type")
            username = service_info.get("username")
            process_id = service_info.get("pid")
            binary_path = service_info.get("binpath")

            timestamp = datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )

            service_data = {
                "Timestamp": timestamp,
                "Service_Name": service_name,
                "Display_Name": display_name,
                "Status": status,
                "Start_Type": start_type,
                "Username": username,
                "PID": process_id,
                "Binary_Path": binary_path
            }

            service_list.append(service_data)

            normalized_path = (binary_path or "").lower()

            suspicious_locations = [
                "\\temp\\",
                "\\appdata\\local\\temp\\",
                "\\downloads\\"
            ]

            for location in suspicious_locations:
                if location in normalized_path:
                    alert = {
                        "Timestamp": timestamp,
                        "Service_Name": service_name,
                        "Binary_Path": binary_path,
                        "Severity": "HIGH",
                        "Alert": "Service Executable Located in Suspicious Directory"
                    }

                    alerts.append(alert)
                    break

        except (psutil.NoSuchProcess,
                psutil.AccessDenied,
                psutil.ZombieProcess,
                OSError):
            continue

    return service_list, alerts


def display_services(service_list):
    print("\n" + "=" * 80)
    print(" WINDOWS SERVICE AUDIT")
    print("=" * 80)

    print("Total Services Detected:", len(service_list))

    for service in service_list:
        print(
            f"Service: {service['Service_Name']} | "
            f"Status: {service['Status']} | "
            f"Start Type: {service['Start_Type']} | "
            f"PID: {service['PID']}"
        )


def display_service_alerts(alerts):
    print("\n" + "=" * 80)
    print(" SUSPICIOUS SERVICE ALERTS")
    print("=" * 80)

    if not alerts:
        print("No suspicious service paths detected.")
    else:
        for alert in alerts:
            print("\n[", alert["Severity"], "]", alert["Alert"])
            print("Service Name:", alert["Service_Name"])
            print("Binary Path:", alert["Binary_Path"])
            print("Timestamp:", alert["Timestamp"])

    print("\nTotal Service Alerts:", len(alerts))


if __name__ == "__main__":
    services, alerts = audit_services()

    display_services(services)
    display_service_alerts(alerts)
