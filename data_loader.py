import csv

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

    input("\nPress Enter to return to the main menu...")
    return data

# Only job: load and prepare data

# Responsibilities:
# Read CSV
# Convert types (int, date, datetime)
# Handle missing values
# Return structured data (list of dicts)

row_headings = ['video_id', 'trending_date', 'title', 'channel_title', 'category_id', 'publish_time', 'tags', 'views', 'likes',
             'dislikes', 'comment_count', 'thumbnail_link', 'comments_disabled', 'ratings_disabled', 'video_error_or_removed', 'description']
