
import os
import winreg

def check_registry_run_keys():
    """Check Windows Registry Run keys."""

    print("\n" + "=" * 60)
    print(" REGISTRY STARTUP ENTRIES")
    print("=" * 60)

    registry_locations = [
        (winreg.HKEY_CURRENT_USER,
         r"Software\Microsoft\Windows\CurrentVersion\Run",
         "HKCU Run"),

        (winreg.HKEY_LOCAL_MACHINE,
         r"Software\Microsoft\Windows\CurrentVersion\Run",
         "HKLM Run"),

        (winreg.HKEY_CURRENT_USER,
         r"Software\Microsoft\Windows\CurrentVersion\RunOnce",
         "HKCU RunOnce"),

        (winreg.HKEY_LOCAL_MACHINE,
         r"Software\Microsoft\Windows\CurrentVersion\RunOnce",
         "HKLM RunOnce")
    ]

    total_entries = 0

    for hive, path, name in registry_locations:

        try:
            key = winreg.OpenKey(hive, path)

            print(f"\n[{name}]")

            index = 0

            while True:
                try:
                    entry_name, entry_value, _ = winreg.EnumValue(
                        key, index
                    )

                    print(f"Name: {entry_name}")
                    print(f"Command: {entry_value}")

                    total_entries += 1
                    index += 1

                except OSError:
                    break

            winreg.CloseKey(key)

        except FileNotFoundError:
            print(f"\n[{name}] No entries found.")

        except PermissionError:
            print(f"\n[{name}] Permission denied.")

    print(f"\nTotal Registry Startup Entries: {total_entries}")


def check_startup_folders():
    """Check Windows Startup folders."""

    print("\n" + "=" * 60)
    print(" STARTUP FOLDER MONITOR")
    print("=" * 60)

    startup_folders = [
        os.path.expandvars(
            r"%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup"
        ),
        os.path.expandvars(
            r"%ProgramData%\Microsoft\Windows\Start Menu\Programs\Startup"
        )
    ]

    total_files = 0

    for folder in startup_folders:

        print(f"\nFolder: {folder}")

        if os.path.exists(folder):

            files = os.listdir(folder)

            if files:
                for file_name in files:
                    print(f"[STARTUP ITEM] {file_name}")
                    total_files += 1
            else:
                print("No startup items found.")

        else:
            print("Folder does not exist.")

    print(f"\nTotal Startup Folder Items: {total_files}")


def main():

    print("=" * 60)
    print(" WINDOWS STARTUP PERSISTENCE MONITOR")
    print("=" * 60)

    check_registry_run_keys()
    check_startup_folders()

    print("\n" + "=" * 60)
    print(" STARTUP MONITORING COMPLETED")
    print("=" * 60)


if __name__ == "__main__":
    main()
