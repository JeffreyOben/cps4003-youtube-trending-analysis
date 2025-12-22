def display_menu():
	# prints menu in the terminal
	print("=" * 40)
	print("   YouTube Trending Videos Analysis")
	print("="*40)
	print("1. Load Data")
	print("2. Basic Processing (Summary Stats)")
	print("3. Intermediate Processing (Averages/Ratios)")
	print("4. Visualisations (Charts)")
	print("5. Export Data (JSON/CSV)")
	print("6. Exit")

def get_choice():
	choice = input("\nEnter your choice (1-6): ")
	return choice

# Text-based UI helper functions

# Print menu
# Get user input
# Validate choices