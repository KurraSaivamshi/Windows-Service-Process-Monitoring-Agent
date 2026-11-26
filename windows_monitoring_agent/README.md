\# Windows Service \& Process Monitoring Agent



\## 1. Project Overview



The \*\*Windows Service \& Process Monitoring Agent\*\* is a Python-based cybersecurity monitoring project designed to monitor Windows processes, services, startup activities, security events, and file integrity.



The project collects system information, identifies potentially suspicious activity using predefined detection rules, and generates security alerts and reports.



It is developed as an educational cybersecurity project to demonstrate basic endpoint monitoring and security auditing techniques.



\## 2. Project Objectives



\- Monitor running Windows processes.

\- Identify suspicious parent-child process relationships.

\- Audit Windows services and their executable paths.

\- Detect processes running from potentially unauthorized locations.

\- Monitor Windows Security Event Logs.

\- Detect file creation, modification, and deletion using SHA-256 hashes.

\- Identify common Windows startup persistence locations.

\- Maintain centralized security alerts.

\- Generate security monitoring reports.



\## 3. Technologies Used



| Technology | Purpose |

|---|---|

| Python 3 | Main programming language |

| psutil | Process and service monitoring |

| hashlib | SHA-256 file integrity checking |

| JSON | Baseline storage |

| CSV | Security alert storage |

| PowerShell | Windows Security Event Log access |

| Windows Registry | Startup persistence auditing |

| OS and subprocess modules | System operations and module execution |



\## 4. Project Modules



The project contains 11 Python modules.



| No. | Module | Description |

|---|---|---|

| 1 | process\_monitor.py | Collects running process information. |

| 2 | process\_analyzer.py | Checks suspicious parent-child process relationships. |

| 3 | service\_auditor.py | Audits Windows services and executable paths. |

| 4 | unauthorized\_process\_monitor.py | Checks processes running from potentially suspicious locations. |

| 5 | security\_report.py | Generates a security monitoring report. |

| 6 | main.py | Executes five core modules through a central orchestrator. |

| 7 | continuous\_monitor.py | Performs repeated process monitoring. |

| 8 | event\_log\_monitor.py | Checks selected Windows Security Event IDs. |

| 9 | file\_integrity\_monitor.py | Detects new, modified, and deleted files using SHA-256 hashes. |

| 10 | startup\_persistence\_monitor.py | Audits Registry startup entries and Startup folders. |

| 11 | alertlog.py | Records and displays centralized security alerts. |



\## 5. Project Folder Structure



```text

windows\_monitoring\_agent/

│

├── monitored\_files/

│

├── process\_monitor.py

├── process\_analyzer.py

├── service\_auditor.py

├── unauthorized\_process\_monitor.py

├── security\_report.py

├── main.py

├── continuous\_monitor.py

├── event\_log\_monitor.py

├── file\_integrity\_monitor.py

├── startup\_persistence\_monitor.py

├── alertlog.py

├── project\_validator.py

│

├── file\_integrity\_baseline.json

├── security\_alerts.csv

├── security\_monitoring\_report.txt

├── PROJECT\_DOCUMENTATION.txt

└── README.md

```



Additional CSV or JSON files may be generated when the monitoring modules execute.



\## 6. Installation Requirements



\- Windows 10 or Windows 11

\- Python 3.10 or compatible Python version

\- PowerShell

\- Visual Studio Code or another Python editor



Install the required Python library:



```powershell

python -m pip install psutil

```



\## 7. How to Run the Project



Open PowerShell and navigate to the project directory:



```powershell

cd "C:\\Users\\YOUR\_USERNAME\\Desktop\\windows\_monitoring\_agent"

```



Run the main monitoring application:



```powershell

python main.py

```



The main program executes these five core modules:



1\. Process Monitoring

2\. Suspicious Process Analysis

3\. Windows Service Auditing

4\. Unauthorized Process Monitoring

5\. Security Report Generation



\## 8. Running Additional Monitoring Modules



The remaining monitoring modules can be executed separately.



\*\*Continuous Process Monitoring\*\*



```powershell

python continuous\_monitor.py

```



Press Ctrl + C to stop monitoring.



\*\*Windows Security Event Log Monitoring\*\*



```powershell

python event\_log\_monitor.py

```



Administrator privileges may be required depending on Windows permissions.



\*\*File Integrity Monitoring\*\*



```powershell

python file\_integrity\_monitor.py

```



Place files inside `monitored\_files` to monitor them.



The first run creates a SHA-256 baseline. Subsequent runs compare the current files against the saved baseline.



\*\*Startup Persistence Monitoring\*\*



```powershell

python startup\_persistence\_monitor.py

```



\*\*Centralized Alert Logger\*\*



```powershell

python alertlog.py

```



\## 9. File Integrity Monitoring



The File Integrity Monitor uses the SHA-256 cryptographic hash algorithm.



It supports three detection functions:



\- New file detection

\- Modified file detection

\- Deleted file detection



The initial scan creates a baseline in:



```text

file\_integrity\_baseline.json

```



Subsequent scans compare current file hashes against the saved baseline.



\## 10. Windows Security Event Monitoring



The Event Log Monitor checks selected Windows Security Event IDs:



| Event ID | Description |

|---|---|

| 4625 | Failed logon attempt |

| 4688 | Process creation |

| 5379 | Credential Manager credentials were read |



These events provide useful security investigation information. They do not automatically indicate malicious activity.



\## 11. Testing and Validation



The following tests were performed during project validation:



\- Process monitoring execution

\- Suspicious process analysis execution

\- Windows service auditing execution

\- Unauthorized process monitoring execution

\- Security report generation

\- Continuous process monitoring

\- Security Event Log monitoring

\- File integrity modification detection

\- File integrity new file detection

\- File integrity deleted file detection

\- Startup persistence monitoring

\- Centralized alert logging



\### Final Validation Results



| Test | Result |

|---|---|

| Project module files | 11 found, 0 missing |

| Main integration test | 5 modules successful, 0 failed |

| File integrity detection | New, modified, and deleted file tests passed |

| Startup persistence monitor | Executed successfully |

| Centralized alert logger | Executed successfully |

| Project validator | Passed |



\## 12. Limitations



\- Detection is based on predefined rules and basic heuristics.

\- The project is not a replacement for commercial Endpoint Detection and Response (EDR) software.

\- Some Windows operations require administrator privileges.

\- Legitimate applications may trigger false-positive alerts.

\- Security Event ID detection depends on available Windows audit logs.

\- Continuous monitoring currently focuses on process activity.

\- The main orchestrator does not automatically execute every standalone module.



\## 13. Future Enhancements



\- Real-time Windows process monitoring.

\- Email notifications for high-severity alerts.

\- Improved behavioral detection rules.

\- Integration with a SIEM platform.

\- Automated security dashboard.

\- Network traffic monitoring.

\- Threat intelligence integration.

\- Improved alert correlation and severity classification.



\## 14. Conclusion



The Windows Service \& Process Monitoring Agent demonstrates fundamental endpoint security monitoring concepts using Python.



The project provides practical experience in process analysis, Windows service auditing, security event monitoring, startup persistence auditing, file integrity monitoring, and security reporting.



It serves as an educational foundation for further development in endpoint security, threat detection, and Security Operations Center (SOC) monitoring.



\---



\*\*Project:\*\* Windows Service \& Process Monitoring Agent  

\*\*Category:\*\* Cybersecurity / Endpoint Security Monitoring  

\*\*Language:\*\* Python  

\*\*Platform:\*\* Windows

