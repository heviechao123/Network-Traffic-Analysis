
# Network Traffic Analysis

## Project Overview

Network Traffic Analysis is a Python-based cybersecurity project that captures, monitors, and analyzes network traffic to identify potentially suspicious activities and unusual communication patterns.

The project uses packet sniffing, traffic analysis, basic threat detection techniques, and data visualization to understand network behavior.

## Objective

To capture and analyze network traffic to identify unusual patterns, potential malware indicators, and signs of suspicious network activity.

## Tools and Technologies

- Python
- Scapy
- Pandas
- Matplotlib
- Wireshark
- Npcap

## Project Features

### 1. Network Packet Capture
- Captures live network packets.
- Extracts source and destination IP addresses.
- Identifies network protocols.
- Records source and destination ports.
- Measures packet sizes.
- Saves captured information in CSV format.

### 2. Network Traffic Analysis
- Calculates the total number of captured packets.
- Displays protocol distribution.
- Identifies frequently occurring source IP addresses.
- Identifies frequently occurring destination IP addresses.
- Calculates average, minimum, and maximum packet sizes.
- Calculates total captured data.

### 3. Threat Detection
Checks network traffic for potentially suspicious patterns:

- Unusual destination ports.
- Repeated packets from a source IP address.
- Packets larger than 1500 bytes.

Potential security alerts are displayed in the terminal and saved in a text report.

**Note:** These checks are basic detection techniques. Alerts require further investigation and do not independently confirm malicious activity.

### 4. Data Visualization
Generates graphical representations of network traffic:

- Network Protocol Distribution
- Top 5 Source IP Addresses

Graphs are generated using Matplotlib and saved as PNG files.

### 5. Main Menu
A central menu allows users to execute the different project modules from one program.

## Project Directory Structure

```text
Network-Traffic-Analysis/
│
├── data/
│   └── captured_traffic.csv
│
├── reports/
│   ├── threat_report.txt
│   ├── protocol_distribution.png
│   └── top_source_ips.png
│
├── main.py
├── packet_capture.py
├── packet_analysis.py
├── threat_detection.py
├── visualization.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation Requirements

- Python 3.x
- Visual Studio Code
- Windows operating system
- Npcap installed for Windows packet capture
- Required Python libraries

## Installation and Execution

### Step 1: Open the Project

Open the project folder in Visual Studio Code.

### Step 2: Create a Virtual Environment

```bash
python -m venv .venv
```

### Step 3: Activate the Virtual Environment

For Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

For Windows Command Prompt:

```cmd
.venv\Scripts\activate.bat
```

### Step 4: Install Required Libraries

```bash
pip install -r requirements.txt
```

### Step 5: Execute the Project

```bash
python main.py
```

### Step 6: Select an Operation

Choose an option from the main menu:

1. Capture Network Traffic
2. Analyze Network Traffic
3. Detect Potential Threats
4. Generate Traffic Graphs
5. Run Complete Analysis
6. Exit

Run packet capture with the permissions required by your Windows and Npcap configuration.

## Sample Threat Detection Output

```text
===================================
        THREAT DETECTION
===================================

Potential security alerts:

[WARNING] Large packets detected: 1

===================================
       SCAN COMPLETED
===================================
```

This is an example of a packet-size threshold alert and does not necessarily indicate a security attack.

## Generated Output Files

| File | Description |
|---|---|
| captured_traffic.csv | Captured network packet information |
| threat_report.txt | Potential security alerts |
| protocol_distribution.png | Protocol distribution graph |
| top_source_ips.png | Top source IP addresses graph |

## Skills Learned

- Network packet sniffing
- Network traffic monitoring
- TCP, UDP, DNS, ICMP, and ARP protocol identification
- IP address analysis
- Basic threat detection
- Python programming
- Data analysis using Pandas
- Data visualization using Matplotlib
- Cybersecurity fundamentals

## Conclusion

This project demonstrates the basic process of capturing, analyzing, and monitoring network traffic using Python.

It provides practical experience with packet sniffing, protocol analysis, basic threat detection, and graphical representation of network activity.

## Disclaimer

This project is developed for educational and cybersecurity learning purposes.

Network traffic should only be captured and analyzed on networks where proper authorization has been obtained.
