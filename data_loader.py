import csv
import json

def load_data(file_path):
    print(f"\nLoading CSV file from {file_path}...")
    data = []

    try:
        with open(file_path, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)

        print(f"SUCCESS: {len(data)} rows loaded.")

    except FileNotFoundError:
        print(f"ERROR: File not found: {file_path}")
        data = None

    except Exception as e:
        print(f"ERROR: {e}")
        data = None

    input("\nPress Enter to continue...\n")
    return data
