def basic_analysis(loaded_data):
    print("\n--- Basic Analysis ---")

    if not loaded_data:
        print("No data available.")
        return

    # Total number of videos
    total_videos = len(loaded_data)
    print(f"Total Trending Videos: {total_videos}")

    # Total number of unique channels
    channels = set()
    for row in loaded_data:
        channels.add(row["channel_title"])
    print(f"Total Unique Channels: {len(channels)}")

    # Total number of categories
    categories = set()
    for row in loaded_data:
        categories.add(row["category_id"])
    print(f"Total Categories: {len(categories)}")

    # Each category and its video count
    category_counts = {}
    for row in loaded_data:
        cid = row["category_id"]
        category_counts[cid] = category_counts.get(cid, 0) + 1

    # Top 10 videos by views
    print("\nTop 10 Videos by Views:")
    sorted_by_views = sorted(
        loaded_data, key=lambda x: int(x["views"]), reverse=True
    )

    for i in range(min(10, total_videos)):
        video = sorted_by_views[i]
        print(f"{i + 1}. {video['title']} ({video['views']} views)")

    # Top 10 videos by likes
    print("\nTop 10 Videos by Likes:")
    sorted_by_likes = sorted(
        loaded_data, key=lambda x: int(x["likes"]), reverse=True
    )

    for i in range(min(10, total_videos)):
        video = sorted_by_likes[i]
        print(f"{i + 1}. {video['title']} ({video['likes']} likes)")

    # Top 10 videos by comments
    print("\nTop 10 Videos by Comments:")
    sorted_by_comments = sorted(
        loaded_data, key=lambda x: int(x["comment_count"]), reverse=True
    )

    for i in range(min(10, total_videos)):
        video = sorted_by_comments[i]
        print(
            f"{i + 1}. {video['title']} ({video['comment_count']} comments)"
        )

    input("\nPress Enter to return...\n")


def intermediate_analysis(loaded_data):
    print("\n--- Intermediate Analysis ---")

    if not loaded_data:
        return

    # Calculate Average Views and Likes
    total_views = 0
    total_likes = 0
    for row in loaded_data:
        views = int(row['views'])  # Convert to int
        likes = int(row['likes'])  # Convert to int

        total_views += views
        total_likes += likes

    avg_views = total_views / len(loaded_data)
    avg_likes = total_likes / len(loaded_data)

    print(f"Average Views: {avg_views:,.2f}")
    print(f"Average Likes: {avg_likes:,.2f}")

    # Likes to Views Ratio (Engagement)
    if total_views > 0:
        engagement_rate = (total_likes / total_views) * 100
        print(f"Overall Engagement Rate (Likes/Views): {engagement_rate:.2f}%")

    # Category distribution (Top 3)
    categories = {}
    for row in loaded_data:
        cat_id = row['category_id']
        categories[cat_id] = categories.get(cat_id, 0) + 1

    print("\nVideos per Category ID (Top 3):")
    sorted_cats = sorted(categories.items(), key=lambda x: x[1], reverse=True)
    for i in range(min(3, len(sorted_cats))):
        cat_id, count = sorted_cats[i]
        print(f"Category {cat_id}: {count} videos")

    input("\nPress Enter to return...\n")


def get_video_details(loaded_data):
    video_id = input("\nEnter video id: ").strip()

    for row in loaded_data:
        if row["video_id"] == video_id:
            print("\n--- Video Details ---")
            print(f"Title: {row['title']}")
            print(f"Channel: {row['channel_title']}")
            print(f"Category ID: {row['category_id']}")
            print(f"Views: {row['views']}")
            print(f"Likes: {row['likes']}")
            print(f"Comments: {row['comment_count']}")
            print(f"Published At: {row['publish_time']}")
            print(f"Description: {row['description']}")
            print(f"Tags: {row['tags']}")
            input("\nPress Enter to return...\n")
            return
        
    print("Video ID not found.")
    input("\nPress Enter to return...\n")

def advanced_analysis(loaded_data):
    print("\n--- Advance Analysis ---")

    if not loaded_data:
        print("No data available.")
        return

        # Implement a recommendation feature that suggests similar videos based on shared categories and tags.

        # Analyse tag text using keyword extraction or frequency counts to identify emerging themes and trends.

        # Detect anomalies in engagement patterns, such as videos with extremely high likes but disproportionately low comments and generate actionable insights.

        # Predict the potential trending duration of a video using features such as publish time, category, and early engagement metrics.
