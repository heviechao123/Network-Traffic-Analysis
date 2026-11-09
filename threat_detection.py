
import pandas as pd
from pathlib import Path
from datetime import datetime

def detect_threats():
    project_folder = Path(__file__).resolve().parent
    file_path = project_folder / "data" / "captured_traffic.csv"
    report_folder = project_folder / "reports"

    report_folder.mkdir(exist_ok=True)

    if not file_path.exists():
        print("Error: Traffic CSV file not found!")
        print("Run packet_capture.py first.")
        return

    df = pd.read_csv(file_path)

    if df.empty:
        print("No traffic data available.")
        return

    print("\n===================================")
    print("        THREAT DETECTION")
    print("===================================")

    alerts = []

    # Check 1: Unusual destination ports
    suspicious_ports = [4444, 1337, 6667, 31337]

    for _, packet in df.iterrows():
        if str(packet["Destination Port"]).isdigit():
            port = int(packet["Destination Port"])

            if port in suspicious_ports:
                alerts.append(
                    f"Unusual destination port: {port} "
                    f"(Destination IP: {packet['Destination IP']})"
                )

    # Check 2: Repeated source IP addresses
    source_counts = df["Source IP"].value_counts()

    for ip, count in source_counts.items():
        if ip != "N/A" and count > 20:
            alerts.append(
                f"High packet count from {ip}: {count} packets"
            )

    # Check 3: Large packets
    large_packets = df[df["Packet Size"] > 1500]

    if not large_packets.empty:
        alerts.append(
            f"Large packets detected: {len(large_packets)}"
        )

    # Display scan results
    if alerts:
        print("\nPotential security alerts:\n")
        for alert in alerts:
            print("[WARNING]", alert)
    else:
        print("\nNo suspicious patterns detected by these checks.")

    # Save results to a text report
    report_path = report_folder / "threat_report.txt"

    with open(report_path, "w", encoding="utf-8") as report:
        report.write("NETWORK TRAFFIC ANALYSIS - THREAT REPORT\n")
        report.write("=" * 45 + "\n")
        report.write(
            f"Scan Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n"
        )
        report.write(f"Total Packets Analyzed: {len(df)}\n\n")

        if alerts:
            report.write("POTENTIAL SECURITY ALERTS\n")
            for alert in alerts:
                report.write(f"[WARNING] {alert}\n")
        else:
            report.write("No suspicious patterns detected by these checks.\n")

        report.write(
            "\nNote: These are heuristic alerts and do not confirm "
            "malicious activity.\n"
        )

    print("\nThreat report saved successfully!")
    print(f"Report location: {report_path}")

    print("\n===================================")
    print("       SCAN COMPLETED")
    print("===================================")


if __name__ == "__main__":
    detect_threats()
