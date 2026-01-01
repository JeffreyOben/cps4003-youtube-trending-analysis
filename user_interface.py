def display_menu():
	print("=" * 40)
	print("   YouTube Trending Videos Analysis")
	print("="*40)
	print("1. Load Data")
	print("2. Data Processing")
	print("3. Visualisations (Charts)")
	print("4. Export data")
	print("5. Exit")

def data_processing_menu():
	print("\n--- Data Processing ---")
	print("1. Basic Processing (Summary Stats)")
	print("2. Intermediate Processing (Averages/Ratios)")
	print("3. Advanced Processing ()")
	print("4. Get Video Details")
	print("5. Go Back\n")

# advanced data processing menu
def advanced_data_processing_menu():
	print("\n--- Advanced Data Processing ---")
	print("1. Show Recommendations")
	print("2. Show Tag Analysis")
	print("3. Show Anomaly Detection")
	print("4. Show Predictive Trending Duration")
	print("5. Go Back\n")

def exporter_menu():
	print("\n--- Export Data ---")
	print("1. Export Data (JSON)")
	print("2. Export Data (CSV)")
	print("3. Export Selected Video Details (JSON)")
	print("4. Top 10 Trending Videos (JSON)")
	print("5. Export Video Recommendations (JSON)")
	print("6. Anomaly Detection (JSON)")
	print("7. Predictive Trending Duration (JSON)")
	print("8. Category Engagement Metrics (Filters)")
	print("9. Go Back\n")

# filters menu in the exporter
def filter_menu():
	print("\n--- Filter Data ---")
	print("1. Filter by Category")
	print("2. Filter by Channel")
	print("3. Filter by Trending Period")
	print("4. Go Back\n")

def visualisation_menu():
	print("\n--- Visualisation ---")
	print("1. Basic Visualisations")
	print("2. Intermediate Visualisations")
	print("3. Advanced Visualisations")
	print("4. Go Back\n")

def get_choice():
	choice = input("\nEnter your choice: ")
	return choice