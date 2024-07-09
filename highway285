import requests
import pandas as pd

# Replace with your own API key
API_KEY = 'YAIzaSyBSY2KT8j6iWwiw1ojdLXFHRF-mNBi4NfI'

# List of coordinates for entry points to I-285
entry_points = [
    {"name": "Entry Point 1", "coordinates": "33.89638,-84.25057"},
    {"name": "Entry Point 2", "coordinates": "33.90265,-84.27465"},
    {"name": "Entry Point 3", "coordinates": "33.90277,-84.35827"},
    {"name": "Entry Point 4", "coordinates": "33.90277,-84.35827"},
    {"name": "Entry Point 5", "coordinates": "33.91675,-84.40665"},
    {"name": "Entry Point 6", "coordinates": "33.91504,-84.40664"}.
    {"name": "Entry Point 7", "coordinates": "33.88217,-84.46637"}
]

# List of addresses to check distances from (use your actual addresses here)
addresses = [
    "3311 Catalina Drive, Duluth, GA",
    "3311 Catalina Drive, Chamblee, GA",
    "3311 Catalina Drive, Chamblee, GA",
    "3311 Catalina Drive, Chamblee, GA",
    "6870 Mimms Drive Northwest, Chamblee, GA",
    "6025 Northbelt Pky., Norcross, GA",
    "6450 Jimmy Carter Blvd, Norcross, GA",
    "2760 Pacific Drive, Norcross, GA",
    "1650 Indian Brook Way, Norcross, GA",
    "1760 Corporate Drive, Norcross, GA",
    "1700 Corporate Drive, Norcross, GA",
    "2155 Breckinridge Boulevard, Norcross, GA",
    "195 Sawmill Drive, Lawrenceville, GA",
    "Hurricane Shoals Road, Suwanee, GA",
    "300 Horizon Drive, Lawrenceville",
    "460 Horizon Drive, Suwanee, GA",
    "0 Vista Ridge Drive, Suwanee, GA",
    "1500 Progress Industrial Blvd, Suwanee, GA",
    "00 Gravel Springs Road Bldg 1, Lawrenceville, GA",
    "Lanier Parkway, Buford, GA",
    "Lanier Parkway, Buford, GA",
    "2630 Gravel Springs Road, Buford, GA",
    "2105 Buford Highway, Buford, GA",
    "2961 Gravel Springs Road, Buford, GA",
    "3016-3046 Summer Oak Pl, Buford, GA",
    "4415 Thompson Mill Road, Buford, GA",
    "3157 Buford Highway North East, Buford, GA",
    "Friendship Road, Buford, GA",
    "Friendship Road, Buford, GA",
    "Friendship Road, Buford, GA",
    "6720 Maple Avenue, Buford, GA",
    "6533 McEver Road ‐ 200, Buford, GA",
    "Kilcrease Road, Buford, GA",
    "Kilcrease Road, Auburn, GA",
    "4755 Thurmond Tanner Road, Auburn, GA",
    "4755 Thurmond Tanner Road, Flowery Branch, GA",
    "1530 Broadway Avenue, Flowery Branch, GA",
    "3920 Falcon Parkway, Bldg 100, Braselton, GA",
    "3920 Falcon Parkway, Bldg 200, Oakwood, GA",
    "3920 Falcon Parkway, Bldg 300, Oakwood, GA",
    "5761 McEver Road, Oakwood, GA",
    "4000 Chamblee Road, Oakwood, GA",
    "Patrick Mill Road, Oakwood, GA",
    "Patrick Mill Road, Winder, Ga",
    "Braselton Circuit Building 2, Winder, GA",
    "138 Braselton Parkway, Braselton, GA",
    "138 Braselton Parkway, Braselton, GA",
    "Jesse Cronic Road & I-85, Braselton, GA",
    "Jesse Cronic Road & I-85, Braselton, GA",
    "2490 Atlanta Highway, Braselton, GA",
    "2560 West Park Drive, Gainesville, GA",
    "11084 Lewis Braselton Boulevard, Gainesville, GA",
    "Innovation Drive, Braselton, GA",
    "1220 Palmour Drive, Winder, GA",
    "1900 Fullenwider Road, Gainesville, GA",
    "1900 Fullenwider Road, Gainesville, GA",
    "New Salem Church Road, Gainesville, GA",
    "New Salem Church Road, Jefferon, GA",
    "6000 Athens Highway, Jefferson, GA",
    "6000 Athens Highway, Pendergrass, GA",
    "6000 Athens Highway, Pendergrass, GA",
    "6000 Athens Highway, Pendergrass, GA",
    "Concord Road, Pendergrass, GA",
    "525 Henry D Robinson Blvd, Jefferson, GA",
    "860 John B Brooks Road, Pendergrass, GA",
    "480 Village Parkway, Pendergrass, GA",
    "3104 Athens Highway, Pendergrass, GA",
    "3104 Athens Highway, Gainesville, GA",
    "500 Valentine Industrial Parkway, Gainesville, GA",
    "421 Toy Wright Road, Pendergrass, GA",
    "1725 Wayne Poultry Road, Pendergrass, GA",
    "1727 Wayne Poultry Road, Pendergrass, GA",
    "8206 N Us Highway 129, Pendergrass, GA",
    "355 Horace Head Road, Pendergrass, GA",
    "1015 Dry Pond Road, Jefferson, GA",
    "354 Raco Parkway, Jefferson, GA",
    "354 Raco Parkway, Pendergrass, GA",
    "354 Raco Parkway, Pendergrass, GA",
    "1860 Winder Highway, Pendergrass, GA",
    "668 Thomas Parkway, Jefferson, GA",
    "Jett Roberts Rd, Jefferson, GA",
    "Maysville Road, Jefferson, GA",
    "Maysville Road, Commerce, GA",
    "Maysville Road, Commerce, GA",
    "Nunn Road, Maysville, GA",
    "Nunn Road, Commerce, GA",
    "1532 Ridgeway Church Road, Commerce, GA",
    "2000 Ridgeway Church Road, Commerce, GA",
    "2000 Ridgeway Church Road, Commerce, GA",
    "2000 Ridgeway Church, Commerce, GA",
    "Steve Reynolds Ind Pkwy, Commerce",
    "Steve Reynolds Ind Pkwy, Commerce, GA",
    "21 Cold Sassy Lane, Commerce, GA"
]

# Function to get driving distance and duration from origin to multiple destinations
def get_driving_distance_and_duration(origin, destinations, api_key):
    distances = []
    for destination in destinations:
        url = f"https://maps.googleapis.com/maps/api/distancematrix/json?origins={origin}&destinations={destination['coordinates']}&key={api_key}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if data['rows'][0]['elements'][0]['status'] == 'OK':
                distance_meters = data['rows'][0]['elements'][0]['distance']['value']
                distance_miles = distance_meters * 0.000621371  # Convert meters to miles
                duration_seconds = data['rows'][0]['elements'][0]['duration']['value']
                duration_minutes = duration_seconds / 60  # Convert seconds to minutes
                distances.append({
                    "name": destination['name'],
                    "coordinates": destination['coordinates'],
                    "distance_miles": round(distance_miles, 2),
                    "duration_minutes": round(duration_minutes, 2)
                })
            else:
                distances.append({
                    "name": destination['name'],
                    "coordinates": destination['coordinates'],
                    "distance_miles": "N/A",
                    "duration_minutes": "N/A"
                })
        else:
            distances.append({
                "name": destination['name'],
                "coordinates": destination['coordinates'],
                "distance_miles": "N/A",
                "duration_minutes": "N/A"
            })
    return distances

# Calculate the shortest distance to the closest entry point for each address
results = []
for address in addresses:
    distances = get_driving_distance_and_duration(address, entry_points, API_KEY)
    # Find the entry point with the shortest distance
    shortest_distance = min(distances, key=lambda x: x['distance_miles'] if isinstance(x['distance_miles'], float) else float('inf'))
    results.append({
        "address": address,
        "closest_entry_point": shortest_distance['name'],
        "entry_point_coordinates": shortest_distance['coordinates'],
        "distance_miles": shortest_distance['distance_miles'],
        "duration_minutes": shortest_distance['duration_minutes']
    })

# Create a DataFrame and print the results
df = pd.DataFrame(results)
print(df)

# Save the DataFrame to a CSV file
df.to_csv('closest_entry_points.csv', index=False)
