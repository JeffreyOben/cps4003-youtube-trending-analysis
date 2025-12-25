import data_loader
import data_processing
import exporter
import user_interface
import visualisation

file_path = "data/youtube_trending_videos.csv"

def main():
    loaded_data = None

    while True:
        user_interface.display_menu()
        choice = user_interface.get_choice()

        if choice == "1":
            loaded_data = data_loader.load_data(file_path)
        elif choice == "2":
            if loaded_data:
                data_processing.basic_processing(loaded_data)
            else:
                print("\n !!!Please load data first.\n")
        elif choice == "3":
            if loaded_data:
                data_processing.intermediate_processing(loaded_data)
            else:
                print("\n !!!Please load data first.\n")
        elif choice == "4":
            if loaded_data:
                file_path
                visualisation.visualise(loaded_data)
            else:
                print("\n !!!Please load data first.\n")
        elif choice == "5":
            if loaded_data:
                exporter.export_data(loaded_data)
            else:
                print("\n !!!Please load data first.\n")
        elif choice == "6":
            print("\nExiting the program...")
            break
        else:
            print("!!!Invalid choice. Please try again. choices 1-6\n")


if __name__ == "__main__":
    main()

# Program entry point:
# 1. Starts the app
# 2. Runs the menu loop
# 3. Calls other modules with the loaded data
# 4. Ensures data is loaded before analysis
