def display_menu():
	print("=" * 40)
	print("   YouTube Trending Videos Analysis")
	print("="*40)
	print("1. Load Data")
	print("2. Data Processing")
	print("3. Visualisations (Charts)")
	print("4. Exports")
	print("5. Exit")

def data_processing_menu():
	print("1. Basic Processing (Summary Stats)")
	print("2. Intermediate Processing (Averages/Ratios)")
	print("3. Go Back\n")

def exporter_menu():
	print("1. Export Data (JSON)")
	print("2. Export Data (CSV)")
	print("3. Go Back\n")

def get_choice():
	choice = input("\nEnter your choice: ")
	return choice
