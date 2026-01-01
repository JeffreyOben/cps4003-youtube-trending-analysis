import statistics
import os
import json

json_output_path = "output/exported_data.json"

# export data to csv
def export_data_csv(data):
    if not os.path.exists("output/exports"):
        os.makedirs("output/exports")

        if not data:
            print("No data to export.")

    print("exporting data as csv...")

    # export data to json
def export_data_json(data):
    if not os.path.exists("output/exports"):
        os.makedirs("output/exports")

    if not data:
        print("No data to export.")
        input("Press Enter to return to the main menu...")
        return

    output_path = "output/exports/exported_data.json"

    try:
        with open(output_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

        print(f"SUCCESS: Data exported to {output_path}")

    except Exception as e:
        print(f"ERROR exporting data: {e}")

    input("Press Enter to return to the main menu...\n")
    

# Save a list of the top 10 trending videos, including views, likes, and comments, in CSV or JSON format.
def top_10_trending_videos(loaded_data):
    if not os.path.exists("output/exports"):
        os.makedirs("output/exports")

    if not loaded_data:
        print("No data to export.")
        input("Press Enter to return...")
        return

    output_path = "output/exports/top_10_trending_videos.json"

    # Sort by views (descending)
    sorted_videos = sorted(
        loaded_data,
        key=lambda x: int(x["views"]),
        reverse=True
    )

    top_10 = []

    for video in sorted_videos[:10]:
        top_10.append({
            "video_id": video["video_id"],
            "title": video["title"],
            "channel_title": video["channel_title"],
            "views": video["views"],
            "likes": video["likes"],
            "comment_count": video["comment_count"]
        })

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(top_10, f, indent=4, ensure_ascii=False)

    print(f"\nTop 10 trending videos exported to {output_path}")
    input("Press Enter to return...")


def selected_video_details(loaded_data):
    # Export detailed information for a selected video in JSON format.
    # Ensure export directory exists
    if not os.path.exists("output/exports"):
        os.makedirs("output/exports")

    if not loaded_data:
        print("No data to export.")
        input("Press Enter to return...")
        return

    video_id = input("Enter a video id: ").strip()
    output_path = f"output/exports/{video_id}_video_details.json"

    # Find the video
    for row in loaded_data:
        if row["video_id"] == video_id:
            with open(output_path, "w", encoding="utf-8") as f:
                json.dump(row, f, indent=4, ensure_ascii=False)

            print(f"\nVideo data exported successfully to {output_path}")
            input("Press Enter to return...")
            return

    # If not found
    print("Video ID not found. Nothing was exported.")
    input("Press Enter to return...")

# Export aggregated engagement metrics per category(averages, totals) in JSON format.
def export_category_metrics(loaded_data):
    # Ensure export directory exists
    if not os.path.exists("output/exports"):
        os.makedirs("output/exports")

    if not loaded_data:
        print("No data to export.")
        input("Press Enter to return...")
        return

    output_path = "output/exports/category_engagement_metrics.json"

    category_metrics = {}

    # Aggregate totals per category
    for row in loaded_data:
        cid = row["category_id"]

        if cid not in category_metrics:
            category_metrics[cid] = {
                "video_count": 0,
                "total_views": 0,
                "total_likes": 0,
                "total_comments": 0
            }

        category_metrics[cid]["video_count"] += 1
        category_metrics[cid]["total_views"] += int(row["views"])
        category_metrics[cid]["total_likes"] += int(row["likes"])
        category_metrics[cid]["total_comments"] += int(row["comment_count"])

    # Compute averages
    for cid, data in category_metrics.items():
        count = data["video_count"]
        data["avg_views"] = data["total_views"] / count
        data["avg_likes"] = data["total_likes"] / count
        data["avg_comments"] = data["total_comments"] / count

    # Export to JSON
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(category_metrics, f, indent=4)

    print(f"\nCategory engagement metrics exported to {output_path}")
    input("Press Enter to return...")
    
# Save filtered datasets based on user-selected categories, channels, or trending periods.
def filter_by_category(loaded_data):
    print("Filter by category")

    if not loaded_data:
        print("No data available.")
        input("Press Enter to return...")
        return

    category_id = input("Enter category ID: ").strip()

    filtered = [row for row in loaded_data if row["category_id"] == category_id]

    if not filtered:
        print("No videos found for this category.")
        input("Press Enter to return...")
        return

    os.makedirs("output/exports", exist_ok=True)
    output_path = f"output/exports/category_{category_id}_filtered.json"

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(filtered, f, indent=4, ensure_ascii=False)

    print(f"Filtered data exported to {output_path}")
    input("Press Enter to return...")


def filter_by_channel(loaded_data):
    print("Filter by channel")

    if not loaded_data:
        print("No data available.")
        input("Press Enter to return...")
        return

    channel_title = input("Enter channel title: ").strip()

    filtered = [
        row for row in loaded_data
        if row["channel_title"].lower() == channel_title.lower()
    ]

    if not filtered:
        print("No videos found for this channel.")
        input("Press Enter to return...")
        return

    os.makedirs("output/exports", exist_ok=True)
    output_path = "output/exports/channel_filtered.json"

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(filtered, f, indent=4, ensure_ascii=False)

    print(f"Filtered data exported to {output_path}")
    input("Press Enter to return...")


def filter_by_trending_period(loaded_data):
    print("Filter by trending period")

    if not loaded_data:
        print("No data available.")
        input("Press Enter to return...")
        return

    trending_date = input("Enter trending date (YY.DD.MM): ").strip()

    filtered = [
        row for row in loaded_data
        if row["trending_date"] == trending_date
    ]

    if not filtered:
        print("No videos found for this trending period.")
        input("Press Enter to return...")
        return

    os.makedirs("output/exports", exist_ok=True)
    output_path = f"output/exports/trending_{trending_date}_filtered.json"

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(filtered, f, indent=4, ensure_ascii=False)

    print(f"Filtered data exported to {output_path}")
    input("Press Enter to return...")


# Export recommendations generated by the system for a selected video, including similar videos based on categories and tags.
def export_recommendations(loaded_data):
    if not os.path.exists("output/exports"):
        os.makedirs("output/exports")

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
    selected_tags = set(selected_video["tags"].lower().split("|"))

    recommendations = []

    for row in loaded_data:
        if row["video_id"] == video_id:
            continue

        score = 0

        # Same category
        if row["category_id"] == selected_category:
            score += 1

        # Shared tags
        row_tags = set(row["tags"].lower().split("|"))
        shared_tags = selected_tags.intersection(row_tags)
        score += len(shared_tags)

        if score > 0:
            recommendations.append({
                "video_id": row["video_id"],
                "title": row["title"],
                "channel_title": row["channel_title"],
                "category_id": row["category_id"],
                "shared_tag_count": len(shared_tags),
                "similarity_score": score
            })

    # Sort by similarity score
    recommendations = sorted(
        recommendations,
        key=lambda x: x["similarity_score"],
        reverse=True
    )[:10]

    output_path = f"output/exports/recommendations_{video_id}.json"

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(recommendations, f, indent=4, ensure_ascii=False)

    print(f"\nRecommendations exported to {output_path}")
    input("Press Enter to return...")
# Recommendations were generated using a content-based approach by matching videos within the same category and calculating tag overlap to determine similarity scores


# Save anomaly detection results, including flagged videos with unusual engagement patterns, in a structured JSON report.
def export_anomaly_detection(loaded_data):
    if not os.path.exists("output/exports"):
        os.makedirs("output/exports")

    if not loaded_data:
        print("No data available.")
        input("Press Enter to return...")
        return

    # Compute engagement ratios (likes-to-dislikes)
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
                "video_id": row["video_id"],
                "title": row["title"],
                "channel_title": row["channel_title"],
                "category_id": row["category_id"],
                "views": row["views"],
                "likes": row["likes"],
                "dislikes": row["dislikes"],
                "likes_to_dislikes_ratio": round(ratio, 2)
            })

    output_path = "output/exports/anomaly_detection_report.json"

    report = {
        "threshold_definition": "mean + 2 * standard deviation",
        "mean_ratio": round(mean_ratio, 2),
        "std_ratio": round(std_ratio, 2),
        "threshold": round(threshold, 2),
        "anomaly_count": len(anomalies),
        "flagged_videos": anomalies
    }

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=4, ensure_ascii=False)

    print(f"\nAnomaly detection report exported to {output_path}")
    input("Press Enter to return...")
# Anomaly detection was performed by calculating likes-to-dislikes ratios and identifying videos exceeding a statistical threshold defined as the mean plus two standard deviations.

# Export predictive trending duration results for videos, allowing further analysis or integration with other systems.
def export_predictive_trending_duration(loaded_data):
    if not os.path.exists("output/exports"):
        os.makedirs("output/exports")

    if not loaded_data:
        print("No data available.")
        input("Press Enter to return...")
        return

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
            "video_id": row["video_id"],
            "title": row["title"],
            "category_id": row["category_id"],
            "views": views,
            "likes": likes,
            "comments": comments,
            "engagement_score": engagement_score,
            "predicted_trending_duration_days": predicted_days
        })

    output_path = "output/exports/predictive_trending_duration.json"

    report = {
        "prediction_method": "heuristic engagement-based estimation",
        "description": "Trending duration estimated using weighted engagement metrics (views, likes, comments)",
        "total_videos_analyzed": len(predictions),
        "predictions": predictions
    }

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=4, ensure_ascii=False)

    print(f"\nPredictive trending duration exported to {output_path}")
    input("Press Enter to return...")
# Trending duration was predicted using a heuristic model based on weighted engagement metrics, allowing relative comparison of potential longevity across videos.