import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
from wordcloud import WordCloud
from datetime import datetime

sns.set_theme(style="whitegrid")  # Seaborn styling

# ------------------------------
# Basic Visualisations
# ------------------------------


def basic_visualisations(loaded_data):
    while True:
        print("\n--- Basic Visualisations ---")
        print("1. Category Distribution (Pie Chart)")
        print("2. Engagement Histograms")
        print("3. Go Back")
        choice = input("\nEnter your choice: ")

        if choice == "1":
            plot_category_distribution(loaded_data)
        elif choice == "2":
            plot_engagement_histograms(loaded_data)
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

# Display a pie chart showing the distribution of videos across all categories.


def plot_category_distribution(data):
    categories = [video.get('category_id', 'Unknown') for video in data]
    counts = Counter(categories)

    labels = []
    sizes = []

    total = sum(counts.values())
    other_count = 0

    for cat, count in counts.items():
        percentage = (count / total) * 100
        if percentage < 3:
            other_count += count
        else:
            labels.append(f"ID {cat}")
            sizes.append(count)

    if other_count > 0:
        labels.append("Other")
        sizes.append(other_count)

    fig, ax = plt.subplots(figsize=(9, 9))

    wedges, texts, autotexts = ax.pie(
        sizes,
        labels=labels,
        autopct="%1.1f%%",
        startangle=140,
        pctdistance=0.75,
        labeldistance=1.05
    )

    # Donut hole
    centre_circle = plt.Circle((0, 0), 0.65, fc="white")
    ax.add_artist(centre_circle)

    ax.set_title("Video Distribution by Category ID", fontsize=14)

    for text in texts:
        text.set_fontsize(9)
    for autotext in autotexts:
        autotext.set_fontsize(9)

    plt.tight_layout()
    plt.show()
# The pie chart visualizes the proportion of trending videos across different categories, highlighting the most dominant genres in the dataset.

# Generate histograms of key engagement metrics, including views, likes, and comment counts.


def plot_engagement_histograms(data):
    views = [int(video.get('views', 0)) for video in data]
    likes = [int(video.get('likes', 0)) for video in data]
    comments = [int(video.get('comment_count', 0)) for video in data]

    plt.figure(figsize=(12, 4))

    plt.subplot(1, 3, 1)
    sns.histplot(views, bins=20, kde=True)
    plt.title("Views Distribution")

    plt.subplot(1, 3, 2)
    sns.histplot(likes, bins=20, kde=True)
    plt.title("Likes Distribution")

    plt.subplot(1, 3, 3)
    sns.histplot(comments, bins=20, kde=True)
    plt.title("Comments Distribution")

    plt.tight_layout()
    plt.show()
# Histograms display the frequency distribution of views, likes, and comments, helping to identify common engagement ranges and skewness in the data.

# ------------------------------
# Intermediate Visualisations
# ------------------------------


def intermediate_visualisations(loaded_data):
    while True:
        print("\n--- Intermediate Visualisations ---")
        print("1. Trending Duration Over Time")
        print("2. Top Video Engagement")
        print("3. Go Back")
        choice = input("\nEnter your choice: ")

        if choice == "1":
            plot_trending_duration_line(loaded_data)
        elif choice == "2":
            plot_top_video_engagement_grouped(loaded_data)
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

# Produce line charts illustrating the average trending duration for each category over time.


def plot_trending_duration_line(data):
    # Compute trending duration per video
    video_dates = {}
    for video in data:
        vid = video['video_id']
        trending_date = datetime.strptime(video['trending_date'], "%y.%d.%m")
        video_dates.setdefault(vid, []).append(trending_date)

    # Compute duration in days per video
    video_duration = {vid: (max(dates) - min(dates)).days +
                      1 for vid, dates in video_dates.items()}

    # Aggregate duration by category_id
    category_duration = {}
    for video in data:
        vid = video['video_id']
        cat = video.get('category_id', 'Unknown')
        duration = video_duration[vid]
        category_duration.setdefault(cat, []).append(duration)

    avg_duration = {cat: sum(durations)/len(durations)
                    for cat, durations in category_duration.items()}

    plt.figure(figsize=(8, 6))
    sns.lineplot(x=list(avg_duration.keys()), y=list(
        avg_duration.values()), marker="o")
    plt.title("Average Trending Duration by Category")
    plt.xlabel("Category ID")
    plt.ylabel("Average Days Trending")
    plt.xticks(rotation=45)
    plt.show()
# The line chart tracks the average trending duration for each category, revealing which types of content tend to stay trending for longer periods.

# Create bar charts comparing engagement metrics(likes, dislikes, comments) across the top-performing videos.


def plot_top_video_engagement_grouped(data):
    # Top 10 videos by views
    top_videos = sorted(data, key=lambda x: int(x['views']), reverse=True)[:10]

    titles = [
        v['title'][:15] + "..." if len(v['title']) > 15 else v['title']
        for v in top_videos
    ]
    likes = [int(v['likes']) for v in top_videos]
    dislikes = [int(v['dislikes']) for v in top_videos]
    comments = [int(v['comment_count']) for v in top_videos]

    x = range(len(titles))
    width = 0.25

    plt.figure(figsize=(12, 6))
    plt.bar([p - width for p in x], likes,
            width=width, label="Likes", color='green')
    plt.bar(x, dislikes, width=width, label="Dislikes", color='red')
    plt.bar([p + width for p in x], comments,
            width=width, label="Comments", color='blue')

    plt.xticks(x, titles, rotation=45)
    plt.title("Top 10 Video Engagement Metrics (Grouped)")
    plt.ylabel("Count")
    plt.legend()
    plt.show()
# The grouped bar chart compares likes, dislikes, and comments for the top 10 videos, offering a direct comparison of engagement intensity.

# ------------------------------
# Advanced Visualisations
# ------------------------------
# Develop an interactive dashboard that allows users to explore key trends, filter by category or channel, and dynamically visualise engagement metrics.


def advanced_visualisations(loaded_data):
    while True:
        print("\n--- Advanced Visualisations ---")
        print("1. Engagement Anomalies")
        print("2. Tag Word Cloud")
        print("3. Go Back")
        choice = input("\nEnter your choice: ")

        if choice == "1":
            plot_engagement_anomalies(loaded_data)
        elif choice == "2":
            plot_tag_wordcloud(loaded_data)
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")
# The advanced visualization menu serves as an interactive dashboard, allowing users to navigate through complex insights like anomalies and tag trends.

# Implement visual overlays to highlight anomalies or unusual engagement patterns, such as high likes-to-dislikes ratios or videos with rapid spikes in views.


def plot_engagement_anomalies(data):
    ratios = []
    titles = []

    for video in data:
        dislikes = int(video.get('dislikes', 0)) if int(
            video.get('dislikes', 0)) > 0 else 1
        ratio = int(video.get('likes', 0)) / dislikes
        ratios.append(ratio)
        titles.append(video['title'][:15] +
                      "..." if len(video['title']) > 15 else video['title'])

    plt.figure(figsize=(10, 6))
    sns.barplot(x=titles, y=ratios)
    plt.xticks(rotation=45)
    plt.title("Likes-to-Dislikes Ratio (Anomalies)")
    plt.ylabel("Ratio")
    plt.show()
# This visualization highlights videos with unusual engagement patterns, specifically focusing on likes-to-dislikes ratios to detect anomalies.

# Incorporate tag-based word clouds or frequency charts to visualise trending themes and topics across videos.


def plot_tag_wordcloud(data):
    all_tags = " ".join(
        video['tags'].replace("|", " ")
        for video in data
        if video['tags'] != "[none]"
    )

    wordcloud = WordCloud(
        width=800,
        height=400,
        background_color="white"
    ).generate(all_tags)

    plt.figure(figsize=(12, 6))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.title("Trending Tags Word Cloud")
    plt.show()
# The word cloud visualizes the most frequently used tags, with larger words representing more common topics and trending themes.
