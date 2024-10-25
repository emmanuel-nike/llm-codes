import googlemaps
from operator import itemgetter

# Initialize the Google Maps client with your API key
gmaps = googlemaps.Client(key='AIzaSyDppVwzKibbos6ayH7PBNlLP9rQvQFtKJ4')

def find_closest_rider(user_location, rider_locations):
    distances = []

    for rider in rider_locations:
        # Calculate the distance between user location and rider location
        distance_result = gmaps.distance_matrix(origins=user_location, destinations=rider['location'])
        distance_info = distance_result['rows'][0]['elements'][0]

        if distance_info['status'] == 'OK':
            distance = distance_info['distance']['value']  # Distance in meters
            distances.append((rider['id'], distance))

    # Sort the list of tuples based on the distance
    distances.sort(key=itemgetter(1))

    # Return the ID of the closest rider
    return distances[0][0] if distances else None

# Example usage
user_location = "40.712776, -74.005974"  # New York City
rider_locations = [{'id': 'rider1', 'location': "40.730610, -73.935242"},  # Example rider locations
                   {'id': 'rider2', 'location': "40.758896, -73.985130"}]
closest_rider_id = find_closest_rider(user_location, rider_locations)
print(f"The closest rider ID is {closest_rider_id}")