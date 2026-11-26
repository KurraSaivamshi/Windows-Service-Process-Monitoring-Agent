
import os
import hashlib
import json

# Directory to monitor
MONITOR_DIRECTORY = "monitored_files"

# File to store baseline hashes
BASELINE_FILE = "file_integrity_baseline.json"


def calculate_hash(file_path):
    """Calculate SHA-256 hash of a file."""

    sha256 = hashlib.sha256()

    try:
        with open(file_path, "rb") as file:
            for block in iter(lambda: file.read(4096), b""):
                sha256.update(block)

        return sha256.hexdigest()

    except Exception as error:
        print(f"Error reading file {file_path}: {error}")
        return None


def scan_directory():
    """Scan directory and calculate file hashes."""

    file_hashes = {}

    for root, dirs, files in os.walk(MONITOR_DIRECTORY):

        for file_name in files:

            file_path = os.path.join(root, file_name)

            file_hash = calculate_hash(file_path)

            if file_hash:
                file_hashes[file_path] = file_hash

    return file_hashes


def save_baseline(file_hashes):
    """Save file hashes to JSON."""

    with open(BASELINE_FILE, "w", encoding="utf-8") as file:
        json.dump(file_hashes, file, indent=4)


def create_baseline():
    """Create initial file integrity baseline."""

    print("\nCreating File Integrity Baseline...")

    baseline = scan_directory()

    save_baseline(baseline)

    print(f"Baseline created for {len(baseline)} files.")


def monitor_integrity():
    """Compare current files against saved baseline."""

    print("\nChecking File Integrity...")

    try:
        with open(BASELINE_FILE, "r", encoding="utf-8") as file:
            baseline = json.load(file)

    except (json.JSONDecodeError, OSError):
        print("Baseline is missing or invalid.")
        create_baseline()
        return

    current_files = scan_directory()

    # Initialize an empty baseline
    if not baseline:
        print("Empty baseline detected.")
        create_baseline()
        return

    alerts = 0

    # Detect new and modified files
    for file_path, current_hash in current_files.items():

        if file_path not in baseline:
            print(f"[NEW FILE] {file_path}")
            alerts += 1

        elif current_hash != baseline[file_path]:
            print(f"[MODIFIED FILE] {file_path}")
            alerts += 1

    # Detect deleted files
    for file_path in baseline:

        if file_path not in current_files:
            print(f"[DELETED FILE] {file_path}")
            alerts += 1

    if alerts == 0:
        print("No file integrity changes detected.")

    print(f"\nTotal Integrity Alerts: {alerts}")

    # Update baseline after checking
    save_baseline(current_files)

    print("Baseline updated successfully.")


if __name__ == "__main__":

    os.makedirs(MONITOR_DIRECTORY, exist_ok=True)

    if not os.path.exists(BASELINE_FILE):
        create_baseline()
    else:
        monitor_integrity()
