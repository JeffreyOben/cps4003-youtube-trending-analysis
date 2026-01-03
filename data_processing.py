from collections import Counter
import statistics

# Retrieve the total number of videos and channels in the dataset.
# List all unique video categories and the number of trending videos per category.
# Identify the top 10 trending videos based on key engagement metrics such as views, likes, and comment count.
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
# Basic analysis provides an overview of the dataset by counting total videos, channels, and categories. It also lists the top 10 videos by views, likes, and comments to highlight trending content.

# Calculate average engagement metrics (likes, dislikes, comments) for each category.
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
# Intermediate analysis calculates average views and likes to gauge general engagement. It also shows the distribution of videos across the top categories.

# Retrieve detailed information for a specific video using its video_id or title.
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
# The video details function retrieves and displays detailed metadata for a specific video, including channel, category, and engagement statistics, allowing for focused inspection.

def advanced_analysis(loaded_data):
    print("\n--- Advance Analysis ---")

    if not loaded_data:
        print("No data available.")
        return

# Implement a recommendation feature that suggests similar videos based on shared categories and tags.
def show_recommendations(loaded_data):
    if not loaded_data:
        print("No data available.")
        input("Press Enter to return...")
        return

    video_id = input("Enter video id: ").strip()

    # Find the selected video
    selected_video = None
    for row in loaded_data:
        if row["video_id"] == video_id:
            selected_video = row
            break

    if not selected_video:
        print("Video ID not found.")
        input("Press Enter to return...")
        return

    selected_category = selected_video["category_id"]

    # Handle tags safely
    if selected_video["tags"] != "[none]":
        selected_tags = set(selected_video["tags"].lower().split("|"))
    else:
        selected_tags = set()

    recommendations = []

    for row in loaded_data:
        if row["video_id"] == video_id:
            continue

        score = 0

        # Same category
        if row["category_id"] == selected_category:
            score += 1

        # Shared tags
        if row["tags"] != "[none]":
            row_tags = set(row["tags"].lower().split("|"))
        else:
            row_tags = set()

        shared_tags = selected_tags.intersection(row_tags)
        score += len(shared_tags)

        if score > 0:
            recommendations.append({
                "title": row["title"],
                "channel": row["channel_title"],
                "category_id": row["category_id"],
                "similarity_score": score,
                "shared_tags": list(shared_tags)
            })

    # Sort by similarity score
    recommendations = sorted(
        recommendations,
        key=lambda x: x["similarity_score"],
        reverse=True
    )[:10]

    print("\n--- Recommended Similar Videos ---")

    if not recommendations:
        print("No similar videos found.")
    else:
        for i, rec in enumerate(recommendations, start=1):
            print(f"{i}. {rec['title']}")
            print(f"   Channel: {rec['channel']}")
            print(f"   Category ID: {rec['category_id']}")
            print(f"   Similarity Score: {rec['similarity_score']}")
            if rec["shared_tags"]:
                print(f"   Shared Tags: {', '.join(rec['shared_tags'])}")
            print()

    input("Press Enter to return...")
# The recommendation feature uses a content-based approach, comparing videos by shared category IDs and overlapping tags. Similarity scores are calculated and the top matching videos are presented directly in the terminal interface, allowing users to explore related content without exporting results to external files.


# Analyse tag text using keyword extraction or frequency counts to identify emerging themes and trends.
def show_tag_analysis(loaded_data):
    if not loaded_data:
        print("No data available.")
        input("Press Enter to return...")
        return

    all_tags = []

    for row in loaded_data:
        tags_field = row["tags"]
        if tags_field != "[none]":
            tags = [tag.strip().lower() for tag in tags_field.split("|")]
            all_tags.extend(tags)

    if not all_tags:
        print("No tags found in dataset.")
        input("Press Enter to return...")
        return

    tag_counts = Counter(all_tags)
    top_tags = tag_counts.most_common(10)

    print("\n--- Top 10 Trending Tags ---\n")
    for i, (tag, count) in enumerate(top_tags, start=1):
        print(f"{i}. {tag} ({count} occurrences)")

    input("\nPress Enter to return...")
# Tag analysis identifies emerging trends by counting the frequency of tags across all videos. The top occurring tags are displayed in the terminal to highlight dominant topics and trending themes.

# Detect anomalies in engagement patterns, such as videos with extremely high likes but disproportionately low comments and generate actionable insights.
def show_anomaly_detection(loaded_data):
    if not loaded_data:
        print("No data available.")
        input("Press Enter to return...")
        return

    # Compute likes-to-dislikes ratios
    ratios = []
    video_ratios = []

    for row in loaded_data:
        likes = int(row["likes"])
        dislikes = int(row.get("dislikes", 0))

        if dislikes > 0:
            ratio = likes / dislikes
            ratios.append(ratio)
            video_ratios.append((row, ratio))

    if not ratios:
        print("Not enough data to detect anomalies.")
        input("Press Enter to return...")
        return

    # Statistical threshold (mean + 2*std)
    mean_ratio = statistics.mean(ratios)
    std_ratio = statistics.stdev(ratios)
    threshold = mean_ratio + 2 * std_ratio

    anomalies = []

    for row, ratio in video_ratios:
        if ratio > threshold:
            anomalies.append({
                "title": row["title"],
                "channel": row["channel_title"],
                "category_id": row["category_id"],
                "views": row["views"],
                "likes": row["likes"],
                "dislikes": row["dislikes"],
                "likes_to_dislikes_ratio": round(ratio, 2)
            })

    print("\n--- Anomalous Videos ---")
    print(f"Threshold (mean + 2*std): {round(threshold, 2)}\n")

    if not anomalies:
        print("No anomalies detected.")
    else:
        for i, video in enumerate(anomalies, start=1):
            print(f"{i}. {video['title']}")
            print(f"   Channel: {video['channel']}")
            print(f"   Category ID: {video['category_id']}")
            print(f"   Views: {video['views']}")
            print(f"   Likes: {video['likes']}")
            print(f"   Dislikes: {video['dislikes']}")
            print(
                f"   Likes/Dislikes Ratio: {video['likes_to_dislikes_ratio']}")
            print()

    input("Press Enter to return...")
# Anomaly detection flags videos with unusual engagement patterns, such as high likes-to-dislikes ratios, helping to identify potential outliers or viral anomalies.


# Predict the potential trending duration of a video using features such as publish time, category, and early engagement metrics.
def show_predictive_trending_duration(loaded_data):
    if not loaded_data:
        print("No data available.")
        input("Press Enter to return...")
        return

    print("Predicting trending duration based on engagement metrics...\n")

    predictions = []

    for row in loaded_data:
        views = int(row["views"])
        likes = int(row["likes"])
        comments = int(row["comment_count"])

        # Simple engagement score
        engagement_score = views + (likes * 10) + (comments * 5)

        # Heuristic prediction (days)
        if engagement_score > 10_000_000:
            predicted_days = 10
        elif engagement_score > 5_000_000:
            predicted_days = 7
        elif engagement_score > 1_000_000:
            predicted_days = 5
        else:
            predicted_days = 2

        predictions.append({
            "title": row["title"],
            "channel": row["channel_title"],
            "category_id": row["category_id"],
            "views": views,
            "likes": likes,
            "comments": comments,
            "predicted_trending_days": predicted_days
        })

    # Show results for top 10 by engagement score
    predictions = sorted(predictions, key=lambda x: (
        x["views"] + x["likes"] + x["comments"]), reverse=True)[:10]

    print("--- Predicted Trending Durations (Top 10 Videos) ---\n")

    for i, video in enumerate(predictions, start=1):
        print(f"{i}. {video['title']}")
        print(f"   Channel: {video['channel']}")
        print(f"   Category ID: {video['category_id']}")
        print(
            f"   Views: {video['views']}, Likes: {video['likes']}, Comments: {video['comments']}")
        print(
            f"   Predicted Trending Duration: {video['predicted_trending_days']} days\n")

    input("Press Enter to return...")
# The system estimates a video’s potential trending duration using a heuristic model based on views, likes, and comments. An engagement score is calculated for each video and mapped to a predicted number of trending days.