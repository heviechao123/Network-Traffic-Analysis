
from packet_capture import capture_packets
from packet_analysis import analyze_traffic
from threat_detection import detect_threats
from visualization import visualize_traffic

def main():
    while True:
        print("\n===================================")
        print("     NETWORK TRAFFIC ANALYSIS")
        print("===================================")

        print("1. Capture Network Traffic")
        print("2. Analyze Network Traffic")
        print("3. Detect Potential Threats")
        print("4. Generate Traffic Graphs")
        print("5. Run Complete Analysis")
        print("6. Exit")

        choice = input("\nEnter your choice (1-6): ")

        if choice == "1":
            capture_packets()

        elif choice == "2":
            analyze_traffic()

        elif choice == "3":
            detect_threats()

        elif choice == "4":
            visualize_traffic()

        elif choice == "5":
            print("\nStarting complete analysis...")
            capture_packets()
            analyze_traffic()
            detect_threats()
            visualize_traffic()

        elif choice == "6":
            print("\nThank you for using Network Traffic Analysis!")
            break

        else:
            print("\nInvalid choice. Please enter a number from 1 to 6.")

if __name__ == "__main__":
    main()
