
from scapy.all import sniff, IP, TCP, UDP, ICMP, DNS, ARP
from datetime import datetime
import csv
from pathlib import Path

# Store captured packets
captured_packets = []


def analyze_packet(packet):

    # Extract timestamp
    timestamp = datetime.fromtimestamp(
        float(packet.time)
    ).strftime("%Y-%m-%d %H:%M:%S")

    # Default values
    source_ip = "N/A"
    destination_ip = "N/A"
    source_port = "N/A"
    destination_port = "N/A"
    protocol = "OTHER"

    # Identify IPv4 addresses
    if IP in packet:
        source_ip = packet[IP].src
        destination_ip = packet[IP].dst

    # Identify protocol and ports
    if DNS in packet:
        protocol = "DNS"

    elif TCP in packet:
        protocol = "TCP"
        source_port = packet[TCP].sport
        destination_port = packet[TCP].dport

    elif UDP in packet:
        protocol = "UDP"
        source_port = packet[UDP].sport
        destination_port = packet[UDP].dport

    elif ICMP in packet:
        protocol = "ICMP"

    elif ARP in packet:
        protocol = "ARP"
        source_ip = packet[ARP].psrc
        destination_ip = packet[ARP].pdst

    # Calculate packet size
    packet_size = len(packet)

    # Create packet information
    packet_info = {
        "Timestamp": timestamp,
        "Source IP": source_ip,
        "Destination IP": destination_ip,
        "Protocol": protocol,
        "Source Port": source_port,
        "Destination Port": destination_port,
        "Packet Size": packet_size
    }

    captured_packets.append(packet_info)

    # Display packet information
    print(
        f"{protocol} | {source_ip} -> "
        f"{destination_ip} | Size: {packet_size} bytes"
    )


def capture_packets():

    print("\n===================================")
    print("     NETWORK TRAFFIC ANALYSIS")
    print("===================================")

    print("\nStarting packet capture...")
    print("Capture duration: Maximum 30 seconds")
    print("Maximum packets: 30\n")

    try:
        sniff(
            prn=analyze_packet,
            count=30,
            timeout=30,
            store=False
        )

        print("\nPacket capture completed.")

        save_to_csv()

    except PermissionError:
        print("\nPermission denied!")
        print("Try running VS Code as Administrator.")

    except Exception as error:
        print("\nAn error occurred:", error)


def save_to_csv():

    if not captured_packets:
        print("No packets captured.")
        return

    # Locate data folder
    data_folder = Path(__file__).resolve().parent / "data"
    data_folder.mkdir(exist_ok=True)

    file_path = data_folder / "captured_traffic.csv"

    # Save packet information
    with open(file_path, "w", newline="", encoding="utf-8") as file:

        writer = csv.DictWriter(
            file,
            fieldnames=captured_packets[0].keys()
        )

        writer.writeheader()
        writer.writerows(captured_packets)

    print(f"\nTotal packets captured: {len(captured_packets)}")
    print(f"CSV report saved at: {file_path}")


if __name__ == "__main__":
    capture_packets()
