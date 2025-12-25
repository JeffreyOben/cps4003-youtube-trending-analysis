import os
import json


def export_data_csv():
    print("exporting data as csv...")

    # export data to json
def export_data_json(data, output_path="output/exported_data.json"):
    if not os.path.exists("output"):
        os.makedirs("output")

    if not data:
        print("No data to export.")
        input("Press Enter to return to the main menu...")
        return

    try:
        with open(output_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

        print(f"SUCCESS: Data exported to {output_path}")

    except Exception as e:
        print(f"ERROR exporting data: {e}")

    input("Press Enter to return to the main menu...\n")
