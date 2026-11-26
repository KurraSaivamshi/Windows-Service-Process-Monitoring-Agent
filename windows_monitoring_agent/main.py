
import subprocess
import sys
import os
from datetime import datetime


# List of project modules
MODULES = [
    ("Process Monitoring", "process_monitor.py"),
    ("Suspicious Process Analysis", "process_analyzer.py"),
    ("Windows Service Auditing", "service_auditor.py"),
    ("Unauthorized Process Monitoring", "unauthorized_process_monitor.py"),
    ("Security Report Generation", "security_report.py")
]


def run_module(module_name, script_name):

    print("\n" + "=" * 70)
    print(" RUNNING MODULE:", module_name)
    print("=" * 70)

    if not os.path.exists(script_name):
        print("ERROR: File not found:", script_name)
        return False

    try:
        result = subprocess.run(
            [sys.executable, script_name],
            check=False
        )

        if result.returncode == 0:
            print("\nModule completed:", module_name)
            return True

        else:
            print("\nModule failed:", module_name)
            return False

    except Exception as error:
        print("Error:", error)
        return False


def main():

    print("\n" + "=" * 70)
    print(" WINDOWS SECURITY MONITORING AGENT")
    print("=" * 70)

    print("Start Time:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    successful_modules = 0
    failed_modules = 0

    for module_name, script_name in MODULES:

        success = run_module(module_name, script_name)

        if success:
            successful_modules += 1
        else:
            failed_modules += 1

    print("\n" + "=" * 70)
    print(" MONITORING DASHBOARD SUMMARY")
    print("=" * 70)

    print("Total Modules:", len(MODULES))
    print("Successful Modules:", successful_modules)
    print("Failed Modules:", failed_modules)

    print("End Time:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    if failed_modules == 0:
        print("\nAll monitoring modules executed successfully!")
    else:
        print("\nSome modules failed. Please check the errors above.")


if __name__ == "__main__":
    main()
