# FILE: process_analyzer.py


# Suspicious parent-child process relationships
SUSPICIOUS_RULES = {

    "winword.exe": [
        "powershell.exe",
        "cmd.exe",
        "wscript.exe",
        "cscript.exe",
        "mshta.exe"
    ],

    "excel.exe": [
        "powershell.exe",
        "cmd.exe",
        "wscript.exe",
        "cscript.exe",
        "mshta.exe"
    ],

    "powerpnt.exe": [
        "powershell.exe",
        "cmd.exe",
        "wscript.exe",
        "cscript.exe"
    ],

    "outlook.exe": [
        "powershell.exe",
        "cmd.exe",
        "wscript.exe",
        "cscript.exe"
    ]
}


# Function to analyze parent-child relationships
def analyze_process_tree(process_list):

    alerts = []

    # Create process dictionary using PID
    process_map = {
        process["PID"]: process
        for process in process_list
    }

    # Analyze each process
    for process in process_list:

        parent_pid = process["PPID"]

        # Find parent process
        parent_process = process_map.get(parent_pid)

        if parent_process is None:
            continue

        parent_name = (parent_process["Name"] or "").lower()
        child_name = (process["Name"] or "").lower()

        # Check suspicious relationship
        if child_name in SUSPICIOUS_RULES.get(parent_name, []):

            alert = {
                "Timestamp": process["Timestamp"],
                "Parent_Name": parent_name,
                "Parent_PID": parent_pid,
                "Child_Name": child_name,
                "Child_PID": process["PID"],
                "Severity": "HIGH",
                "Alert": "Suspicious Parent-Child Relationship"
            }

            alerts.append(alert)

    return alerts


# Function to display alerts
def display_alerts(alerts):

    print("\n" + "=" * 80)
    print(" SUSPICIOUS PROCESS RELATIONSHIP ALERTS")
    print("=" * 80)

    if not alerts:

        print("No suspicious parent-child relationships detected.")

    else:

        for alert in alerts:

            print("\n[", alert["Severity"], "]",
                  alert["Alert"])

            print(
                alert["Parent_Name"],
                "(PID:", alert["Parent_PID"], ")",
                "---->",
                alert["Child_Name"],
                "(PID:", alert["Child_PID"], ")"
            )

            print("Timestamp:", alert["Timestamp"])

    print("\nTotal Alerts:", len(alerts))

# Main execution

if __name__ == "__main__":

    from process_monitor import enumerate_processes

    processes = enumerate_processes()

    alerts = analyze_process_tree(processes)

    display_alerts(alerts)
