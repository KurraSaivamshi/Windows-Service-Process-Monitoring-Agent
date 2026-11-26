
import os
from datetime import datetime

# Project modules to validate
project_files = {
    "process_monitor.py": "Process Monitoring",
    "process_analyzer.py": "Process Analyzer",
    "service_auditor.py": "Windows Service Auditor",
    "unauthorized_process_monitor.py": "Unauthorized Process Monitor",
    "security_report.py": "Security Report Generator",
    "main.py": "Main Orchestrator",
    "continuous_monitor.py": "Continuous Process Monitor",
    "event_log_monitor.py": "Security Event Log Monitor",
    "file_integrity_monitor.py": "File Integrity Monitor",
    "startup_persistence_monitor.py": "Startup Persistence Monitor",
    "alertlog.py": "Centralized Alert Logger"
}


def validate_project():

    print("=" * 70)
    print(" WINDOWS SERVICE & PROCESS MONITORING AGENT")
    print(" FINAL PROJECT VALIDATION")
    print("=" * 70)

    total_files = len(project_files)
    existing_files = 0
    missing_files = []

    for file_name, module_name in project_files.items():

        if os.path.exists(file_name):

            print(f"[FOUND]   {module_name} - {file_name}")
            existing_files += 1

        else:

            print(f"[MISSING] {module_name} - {file_name}")
            missing_files.append(file_name)

    print("\n" + "=" * 70)
    print(" PROJECT VALIDATION SUMMARY")
    print("=" * 70)

    print(f"Total Modules: {total_files}")
    print(f"Files Found: {existing_files}")
    print(f"Files Missing: {len(missing_files)}")

    if len(missing_files) == 0:

        print("\n[STATUS] All listed project modules are present.")

    else:

        print("\n[STATUS] Some project files are missing.")

    # Generate documentation
    with open(
        "PROJECT_DOCUMENTATION.txt",
        "w",
        encoding="utf-8"
    ) as file:

        file.write("WINDOWS SERVICE & PROCESS MONITORING AGENT\n")
        file.write("=" * 50 + "\n\n")

        file.write("Project Objective:\n")
        file.write(
            "Monitor Windows processes, services, security events, "
            "startup locations, and file integrity using Python.\n\n"
        )

        file.write("Project Modules:\n")

        for file_name, module_name in project_files.items():

            file.write(f"- {module_name}: {file_name}\n")

        file.write("\nValidation Summary:\n")
        file.write(f"Total Modules: {total_files}\n")
        file.write(f"Files Found: {existing_files}\n")
        file.write(f"Files Missing: {len(missing_files)}\n")

        file.write(
            "\nValidation Date: "
            + datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            + "\n"
        )

        file.write(
            "\nNote: File presence validation does not prove "
            "that every module executes correctly.\n"
        )

    print("\nDocumentation created:")
    print("PROJECT_DOCUMENTATION.txt")

    print("\n" + "=" * 70)
    print(" FINAL VALIDATION COMPLETED")
    print("=" * 70)


if __name__ == "__main__":
    validate_project()
