
import pandas as pd
from pathlib import Path


def analyze_traffic():

    # Locate the captured CSV file
    project_folder = Path(__file__).resolve().parent
    file_path = project_folder / "data" / "captured_traffic.csv"

    # Check whether the file exists
    if not file_path.exists():
        print("Error: Captured traffic CSV file not found!")
        print("Run packet_capture.py first.")
        return

    # Read CSV data
    df = pd.read_csv(file_path)

    if df.empty:
        print("No traffic data available.")
        return

    print("\n===================================")
    print("       TRAFFIC ANALYSIS REPORT")
    print("===================================")

    # 1. Total packets
    total_packets = len(df)
    print(f"\nTotal Packets Captured: {total_packets}")

    # 2. Protocol distribution
    print("\n--- Protocol Distribution ---")
    protocol_counts = df["Protocol"].value_counts()

    for protocol, count in protocol_counts.items():
        print(f"{protocol}: {count}")

    # 3. Top source IP addresses
    print("\n--- Top Source IP Addresses ---")
    source_counts = df["Source IP"].value_counts().head(5)

    print(source_counts.to_string())

    # 4. Top destination IP addresses
    print("\n--- Top Destination IP Addresses ---")
    destination_counts = (
        df["Destination IP"].value_counts().head(5)
    )

    print(destination_counts.to_string())

    # 5. Packet size statistics
    print("\n--- Packet Size Statistics ---")

    average_size = df["Packet Size"].mean()
    largest_size = df["Packet Size"].max()
    smallest_size = df["Packet Size"].min()

    print(f"Average Packet Size: {average_size:.2f} bytes")
    print(f"Largest Packet Size: {largest_size} bytes")
    print(f"Smallest Packet Size: {smallest_size} bytes")

    # 6. Total data transferred in captured packets
    total_data = df["Packet Size"].sum()

    print(f"\nTotal Captured Data: {total_data} bytes")

    print("\n===================================")
    print("       ANALYSIS COMPLETED")
    print("===================================")


if __name__ == "__main__":
    analyze_traffic()
