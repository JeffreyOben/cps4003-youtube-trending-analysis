import data_loader
import data_processing
import exporter
import user_interface
import visualisation

file_path = "data/youtube_trending_videos.csv"
warn = "\n !!!Please load data first.\n"


def main():
    loaded_data = None

    while True:
        user_interface.display_menu()
        choice = user_interface.get_choice()

        if choice == "1":
            loaded_data = data_loader.load_data(file_path)
        elif choice == "2":
            if loaded_data:
                while True:
                    # show data_processing menu
                    user_interface.data_processing_menu()
                    choice = user_interface.get_choice()
                    if choice == "1":
                        data_processing.basic_analysis(loaded_data)
                    elif choice == "2":
                        data_processing.intermediate_analysis(loaded_data)
                    elif choice == "3":
                        data_processing.advanced_analysis(loaded_data)
                    elif choice == "4":
                        data_processing.get_video_details(loaded_data)
                    elif choice == "5":
                        break
                    else:
                        print("!!!Invalid choice. Please try again. choices 1-3\n")
            else:
                print("\n !!!Please load data first.\n")
        elif choice == "3":
            if loaded_data:
                visualisation.visualise_data()
            else:
                print("\n !!!Please load data first.\n")

        elif choice == "4":
            if loaded_data:
                while True:
                    # show exporter menu
                    user_interface.exporter_menu()
                    choice = user_interface.get_choice()
                    if choice == "1":
                        exporter.export_data_json(loaded_data)
                    elif choice == "2":
                        exporter.export_data_csv(loaded_data)
                    elif choice == "3":
                        exporter.selected_video_details(loaded_data)
                    elif choice == "4":
                        exporter.top_10_trending_videos(loaded_data)
                    elif choice == "5":
                        pick_filter_choice(loaded_data)
                    elif choice == "6":
                        break
                    else:
                        print("!!!Invalid choice. Please try again. choices 1-3\n")
            else:
                print("\n !!!Please load data first.\n")
        elif choice == "5":
            print("\nExiting the program...")
            break
        else:
            print("!!!Invalid choice. Please try again. choices 1-6\n")

# handle filter menu actions


def pick_filter_choice(loaded_data):
    while True:
        user_interface.filter_menu()
        choice = user_interface.get_choice()
        if choice == "1":
            exporter.filter_by_category(loaded_data)
        elif choice == "2":
            exporter.filter_by_channel(loaded_data)
        elif choice == "3":
            exporter.filter_by_trending_period(loaded_data)
        elif choice == "4":
            break
        else:
            print("!!!Invalid choice. Please try again. choices 1-4\n")


if __name__ == "__main__":
    main()

# Program entry point:
# 1. Starts the app
# 2. Runs the menu loop
# 3. Calls other modules with the loaded data
# 4. Ensures data is loaded before analysis
