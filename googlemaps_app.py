from flask import Flask, jsonify, request
import googlemaps

app = Flask(__name__)

# Initialize the Google Maps client with your API key
gmaps = googlemaps.Client(key='AIzaSyDppVwzKibbos6ayH7PBNlLP9rQvQFtKJ4')

@app.route('/directions', methods=['GET'])
def get_directions():
    origin = request.args.get('origin')
    destination = request.args.get('destination')
    
    # Get directions between the two points
    directions_result = gmaps.directions(origin, destination)

    return jsonify(directions_result)

@app.route('/geocode_address', methods=['GET'])
def geocode_address():
    address = request.args.get('address')
    if not address:
        return jsonify({'error': 'Address parameter is required'}), 400

    # Geocode an address
    geocode_result = gmaps.geocode(address)

    # Process the result and return it
    if geocode_result:
        return jsonify(geocode_result[0]['geometry']['location'])
    else:
        return jsonify({'error': 'Address not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)