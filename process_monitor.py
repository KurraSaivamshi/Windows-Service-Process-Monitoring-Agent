
# ============================================================
# PROJECT: Windows Service & Process Monitoring Agent
# MODULE 1: Process Enumeration
# FILE: process_monitor.py
# ============================================================

import psutil
from datetime import datetime


# Function to collect active process information
def enumerate_processes():

    process_list = []

    # Get all active processes
    for process in psutil.process_iter(
        ['pid', 'ppid', 'name', 'exe', 'username', 'create_time']
    ):

        try:

            # Collect process details
            process_info = process.info

            # Store process information
            process_data = {
                "PID": process_info.get("pid"),
                "PPID": process_info.get("ppid"),
                "Name": process_info.get("name"),
                "Path": process_info.get("exe"),
                "Username": process_info.get("username"),
                "Timestamp": datetime.now().strftime(
                    "%Y-%m-%d %H:%M:%S"
                )
            }

            process_list.append(process_data)

        except (psutil.NoSuchProcess,
                psutil.AccessDenied,
                psutil.ZombieProcess):

            # Skip inaccessible or terminated processes
            continue

    return process_list


# Function to display process information
def display_processes(process_list):

    print("\n" + "=" * 80)
    print(" WINDOWS PROCESS MONITORING AGENT")
    print("=" * 80)

    print(f"Total Processes Detected: {len(process_list)}")

    print("-" * 80)

    for process in process_list:

        print(
            f"PID: {process['PID']} | "
            f"PPID: {process['PPID']} | "
            f"Name: {process['Name']} | "
            f"User: {process['Username']}"
        )


# Main execution
if __name__ == "__main__":

    processes = enumerate_processes()

    display_processes(processes)
