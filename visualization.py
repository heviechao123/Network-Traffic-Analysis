
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

def visualize_traffic():
    project_folder = Path(__file__).resolve().parent
    csv_file = project_folder / "data" / "captured_traffic.csv"
    output_folder = project_folder / "reports"

    output_folder.mkdir(exist_ok=True)

    if not csv_file.exists():
        print("Traffic CSV file not found!")
        print("Run packet_capture.py first.")
        return

    df = pd.read_csv(csv_file)

    if df.empty:
        print("No traffic data available.")
        return

    # Graph 1: Protocol distribution
    protocol_counts = df["Protocol"].value_counts()

    plt.figure(figsize=(8, 6))
    protocol_counts.plot(kind="bar")
    plt.title("Network Protocol Distribution")
    plt.xlabel("Protocol")
    plt.ylabel("Number of Packets")
    plt.xticks(rotation=0)
    plt.tight_layout()

    protocol_path = output_folder / "protocol_distribution.png"
    plt.savefig(protocol_path)
    plt.show()
    plt.close()

    # Graph 2: Top source IP addresses
    source_counts = (
        df[df["Source IP"] != "N/A"]["Source IP"]
        .value_counts()
        .head(5)
    )

    if not source_counts.empty:
        plt.figure(figsize=(9, 6))
        source_counts.plot(kind="bar")
        plt.title("Top 5 Source IP Addresses")
        plt.xlabel("Source IP Address")
        plt.ylabel("Number of Packets")
        plt.xticks(rotation=30, ha="right")
        plt.tight_layout()

        source_path = output_folder / "top_source_ips.png"
        plt.savefig(source_path)
        plt.show()
        plt.close()

    print("\nGraphs generated successfully!")
    print("Check your reports folder.")

if __name__ == "__main__":
    visualize_traffic()
