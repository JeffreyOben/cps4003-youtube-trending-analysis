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
                    user_interface.data_processing_menu()
                    choice = user_interface.get_choice()

                    if choice == "1":
                        data_processing.basic_analysis(loaded_data)
                    elif choice == "2":
                        data_processing.intermediate_analysis(loaded_data)
                    elif choice == "3":
                        advanced_data_processing_menu(loaded_data)
                    elif choice == "4":
                        data_processing.get_video_details(loaded_data)
                    elif choice == "5":
                        break
                    else:
                        print("!!!Invalid choice. Please try again. choices 1-5\n")
            else:
                print(warn)

        elif choice == "3":
            if loaded_data:
                while True:
                    user_interface.visualisation_menu()
                    choice = user_interface.get_choice()

                    if choice == "1":
                        visualisation.basic_visualisations(loaded_data)
                    elif choice == "2":
                        visualisation.intermediate_visualisations(loaded_data)
                    elif choice == "3":
                        visualisation.advanced_visualisations(loaded_data)
                    elif choice == "4":
                        break
                    else:
                        print("!!!Invalid choice. Please try again. choices 1-4\n")
            else:
                print(warn)

        elif choice == "4":
            if loaded_data:
                while True:
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
                        exporter.export_recommendations(loaded_data)
                    elif choice == "6":
                        exporter.export_anomaly_detection(loaded_data)
                    elif choice == "7":
                        exporter.export_predictive_trending_duration(
                            loaded_data)
                    elif choice == "8":
                        pick_filter_choice(loaded_data)
                    elif choice == "9":
                        break
                    else:
                        print("!!!Invalid choice. Please try again. choices 1-9\n")
            else:
                print(warn)

        elif choice == "5":
            print("\nExiting the program...")
            break

        else:
            print("!!!Invalid choice. Please try again. choices 1-5\n")


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


def advanced_data_processing_menu(loaded_data):
    while True:
        user_interface.advanced_data_processing_menu()
        choice = user_interface.get_choice()

        if choice == "1":
            data_processing.show_recommendations(loaded_data)
        elif choice == "2":
            data_processing.show_tag_analysis(loaded_data)
        elif choice == "3":
            data_processing.show_anomaly_detection(loaded_data)
        elif choice == "4":
            data_processing.show_predictive_trending_duration(loaded_data)
        elif choice == "5":
            break


if __name__ == "__main__":
    main()
