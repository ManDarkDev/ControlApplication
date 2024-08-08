from flask import Flask, request, jsonify  # Import necessary modules from Flask

app = Flask(__name__)  # Initialize a new Flask application

tokens = {}  # Dictionary to store miner tokens

@app.route('/api/login', methods=['POST'])  # Define the /api/login route, accepting POST requests
def login():
    data = request.get_json()  # Get JSON data from the request
    miner_ip = data.get('miner_ip')  # Extract miner IP from the data
    if miner_ip:
        token = f"token_{miner_ip}"  # Generate a token for the miner
        tokens[miner_ip] = token  # Store the token in the tokens dictionary
        return jsonify({"token": token}), 200  # Return the token with a 200 OK status
    return jsonify({"error": "Invalid miner IP"}), 400  # Return an error if miner IP is invalid

@app.route('/api/logout', methods=['POST'])  # Define the /api/logout route, accepting POST requests
def logout():
    data = request.get_json()  # Get JSON data from the request
    miner_ip = data.get('miner_ip')  # Extract miner IP from the data
    if miner_ip in tokens:  # Check if the miner IP has a valid token
        del tokens[miner_ip]  # Delete the token from the tokens dictionary
        return jsonify({"message": "Logged out"}), 200  # Return a success message with a 200 OK status
    return jsonify({"error": "Invalid token"}), 400  # Return an error if the token is invalid

@app.route('/api/curtail', methods=['POST'])  # Define the /api/curtail route, accepting POST requests
def curtail():
    data = request.get_json()  # Get JSON data from the request
    token = data.get('token')  # Extract the token from the data
    mode = data.get('mode')  # Extract the mode from the data
    if token in tokens.values() and mode in ['sleep', 'active']:  # Validate the token and mode
        return jsonify({"message": f"Miner curtailed to {mode} mode"}), 200  # Return a success message
    return jsonify({"error": "Invalid token or mode"}), 400  # Return an error if the token or mode is invalid

@app.route('/api/profileset', methods=['POST'])  # Define the /api/profileset route, accepting POST requests
def profileset():
    data = request.get_json()  # Get JSON data from the request
    token = data.get('token')  # Extract the token from the data
    profile = data.get('profile')  # Extract the profile from the data
    if token in tokens.values() and profile in ['underclock', 'overclock', 'normal']:  # Validate the token and profile
        return jsonify({"message": f"Profile set to {profile}"}), 200  # Return a success message
    return jsonify({"error": "Invalid token or profile"}), 400  # Return an error if the token or profile is invalid

if __name__ == '__main__':  # If this script is run directly, and not imported
    app.run(port=5000)  # Run the Flask app on port 5000
