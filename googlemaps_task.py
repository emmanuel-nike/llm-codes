# from flask import Flask, request, jsonify
# from flask_socketio import SocketIO, emit

# app = Flask(__name__)
# socketio = SocketIO(app)

# # This route is for demonstration purposes
# @app.route('/update-location', methods=['POST'])
# def update_location():
#     driver_id = request.json.get('driver_id')
#     lat = request.json.get('latitude')
#     lng = request.json.get('longitude')

#     # Here you would store the location in the database or in-memory store
#     # For this example, we'll just emit the update to all connected clients
#     emit('location_update', {'driver_id': driver_id, 'latitude': lat, 'longitude': lng}, broadcast=True, namespace='/')

#     return jsonify({'status': 'success'}), 200

# if __name__ == '__main__':
#     socketio.run(app, debug=True)


# from flask import Flask, jsonify
# from flask_socketio import SocketIO, emit
# import googlemaps

# app = Flask(__name__)
# app.config['SECRET_KEY'] = 'secret!'
# socketio = SocketIO(app)

# # Initialize the Google Maps client with your API key
# gmaps = googlemaps.Client(key='YOUR_API_KEY')

# # This route might be called by the driver's app to update their location
# @app.route('/update_location', methods=['POST'])
# def update_location():
#     driver_id = request.form['driver_id']
#     lat = request.form['latitude']
#     lng = request.form['longitude']
    
#     # You can store the driver's location in your database or in-memory store
#     # and then emit the location to the relevant passengers
#     emit('location_update', {'driver_id': driver_id, 'latitude': lat, 'longitude': lng}, broadcast=True, namespace='/ride')

#     return jsonify({'status': 'success'}), 200

# if __name__ == '__main__':
#     socketio.run(app, debug=True)

from flask import Flask, jsonify, request
from flask_socketio import SocketIO, emit
#import googlemaps
#from your_location_tracking_module import get_driver_location

import googlemaps
from flask import Flask, jsonify, request

app = Flask(__name__)

# Initialize the Google Maps client with your API key
gmaps = googlemaps.Client(key='AIzaSyDppVwzKibbos6ayH7PBNlLP9rQvQFtKJ4')

@app.route('/distance', methods=['GET'])
def get_distance():
    origins = request.args.get('origins')  # Format: "lat1,lng1|lat2,lng2|..."
    destinations = request.args.get('destinations')  # Format: "lat1,lng1|lat2,lng2|..."

    # Request distance information from the Distance Matrix API
    distance_matrix_result = gmaps.distance_matrix(origins, destinations)

    # Extract the distance from the result
    rows = distance_matrix_result['rows']
    if rows:
        elements = rows[0]['elements']
        if elements:
            distance_info = elements[0]['distance']
            return jsonify(distance_info)
    
    return jsonify({'status': 'error', 'message': 'Could not calculate distance'}), 500

if __name__ == '__main__':
    app.run(debug=True)