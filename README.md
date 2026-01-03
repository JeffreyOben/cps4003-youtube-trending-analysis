# YouTube Trending Videos Analysis

A comprehensive Python-based tool for analyzing and visualizing YouTube trending video data. This project provides various levels of statistical analysis, interactive charts, and advanced metrics to uncover insights into what makes videos trend.

## Features

### Data Analysis
- **Basic Analysis**: Summary statistics, total videos, unique channels, and top category distribution.
- **Intermediate Analysis**: Average views, likes, and engagement rate (likes-to-views ratio) calculation.
- **Advanced Processing**:
  - **Recommendation System**: Suggests similar videos based on shared categories and tags.
  - **Tag Analysis**: Identifies emerging themes using keyword frequency counts.
  - **Anomaly Detection**: Flags unusual engagement patterns (e.g., extremely high likes-to-dislikes ratios).
  - **Predictive Trending Duration**: Heuristic engagement-based estimation of how long a video might trend.

### Visualizations
- **Basic**: Category distribution (Donut chart) and engagement histograms for views, likes, and comments.
- **Intermediate**: Average trending duration line charts and grouped bar charts for top video engagement.
- **Advanced**: Engagement anomaly overlays and tag-based Word Clouds for trending themes.

### Data Exportation
- Export processed data and advanced reports in **JSON** or **CSV** formats.
- Filter datasets by **Category**, **Channel**, or **Trending Period** before exporting.

## Technologies Used

- **Python 3**: Core application logic.
- **Matplotlib & Seaborn**: High-quality data visualizations.
- **WordCloud**: Visualizing trending tags.
- **Standard Libraries**: `csv`, `json`, `statistics`, `collections`.

## Project Structure

```text
.
├── data/                   # Input CSV datasets
│   └── youtube_trending_videos.csv
├── output/                 # Generated exports and reports
│   └── exports/            # Filtered JSON/CSV files
├── main.py                 # Application entry point
├── data_loader.py          # CSV loading and parsing
├── data_processing.py      # Statistical and advanced analysis logic
├── visualisation.py        # Chart generation logic
├── exporter.py             # Data export and filtering functionality
├── user_interface.py       # Menu-driven CLI definitions
└── requirements.txt        # Project dependencies
```

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/JeffreyOben/cps4003-youtube-trending-analysis.git
   cd cps4003-youtube-trending-analysis
   ```

2. **Create and Activate a Virtual Environment**:
   
   *macOS / Linux*:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

   *Windows*:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install Dependencies** (ensure venv is active):
   ```bash
   pip install -r requirements.txt
   ```

## Usage

**1. Activate the Virtual Environment** (if not already active):

*macOS / Linux*:
```bash
source venv/bin/activate
```

*Windows*:
```bash
venv\Scripts\activate
```

Run the main script to start the interactive menu:

```bash
python main.py
```

### Navigation
1. **Load Data**: Must be performed first to initialize the dataset.
2. **Data Processing**: Explore summary statistics and advanced metrics.
3. **Visualisations**: Generate and view charts.
4. **Export Data**: Save specific insights or filtered data to the `output/` directory.
5. **Exit**: Safely close the application.
