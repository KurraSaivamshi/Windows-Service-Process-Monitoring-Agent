
import subprocess
import json

def monitor_security_events():
    print("=" * 70)
    print(" WINDOWS SECURITY EVENT LOG MONITOR")
    print("=" * 70)

    powershell_command = """
    Get-WinEvent -FilterHashtable @{
        LogName = 'Security'
        Id = 4625, 4688, 5379
    } -MaxEvents 20 -ErrorAction SilentlyContinue |
    Select-Object Id, TimeCreated, Message |
    ConvertTo-Json -Depth 3
    """

    try:
        result = subprocess.run(
            ["powershell", "-NoProfile", "-Command", powershell_command],
            capture_output=True,
            text=True,
            timeout=30
        )

        output = result.stdout.strip()

        if not output:
            print("No matching Security events were found.")
            return

        events = json.loads(output)

        # PowerShell returns a single object when only one event exists
        if isinstance(events, dict):
            events = [events]

        print(f"\nTotal Events Found: {len(events)}\n")

        for event in events:
            event_id = event.get("Id", "Unknown")
            event_time = event.get("TimeCreated", "Unknown")
            message = event.get("Message", "No message available")

            print("-" * 70)
            print(f"Event ID: {event_id}")
            print(f"Time: {event_time}")

            if event_id == 4625:
                print("Alert Type: Failed Logon Attempt")

            elif event_id == 4688:
                print("Alert Type: Process Creation")

            elif event_id == 5379:
                print("Alert Type: Credential Manager Access")

            print("Event Details:")
            print(message[:500])

        print("\n" + "=" * 70)
        print(" SECURITY EVENT MONITORING COMPLETED")
        print("=" * 70)

    except json.JSONDecodeError:
        print("Unable to parse the Security Event Log output.")

    except subprocess.TimeoutExpired:
        print("PowerShell command timed out.")

    except Exception as error:
        print(f"Error monitoring Security Events: {error}")


if __name__ == "__main__":
    monitor_security_events()

