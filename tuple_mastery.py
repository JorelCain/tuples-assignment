# Tuple Mastery

# Formatting Flight Itineraries: Create a Python function that takes a list of tuples as an argument. Each tuple contains information about a flight itinerary: (traveler_name, origin, destination). The function should loop through the list of itineraries and print a formatted string for each. For example, if the input is [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")], the output should be:

itineraries = [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]

def flight_itineraries(itineraries):
	for i, itinerary in enumerate(itineraries, start=1):
		traveler_name, origin, destination = itinerary
		print(f"Itinerary {i}: {traveler_name} - From {origin} to {destination}")
		
flight_itineraries(itineraries)