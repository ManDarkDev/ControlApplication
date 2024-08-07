from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulated database of tokens
tokens = {}

@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    miner_ip = data.get('miner_ip')
    if miner_ip:
        token = f"token_{miner_ip}"
        tokens[miner_ip] = token
        return jsonify({"token": token}), 200
    return jsonify({"error": "Invalid miner IP"}), 400

@app.route('/api/logout', methods=['POST'])
def logout():
    data = request.get_json()
    miner_ip = data.get('miner_ip')
    if miner_ip in tokens:
        del tokens[miner_ip]
        return jsonify({"message": "Logged out"}), 200
    return jsonify({"error": "Invalid token"}), 400

@app.route('/api/curtail', methods=['POST'])
def curtail():
    data = request.get_json()
    token = data.get('token')
    mode = data.get('mode')
    if token in tokens.values() and mode in ['sleep', 'active']:
        return jsonify({"message": f"Miner curtailed to {mode} mode"}), 200
    return jsonify({"error": "Invalid token or mode"}), 400

@app.route('/api/profileset', methods=['POST'])
def profileset():
    data = request.get_json()
    token = data.get('token')
    profile = data.get('profile')
    if token in tokens.values() and profile in ['underclock', 'overclock', 'normal']:
        return jsonify({"message": f"Profile set to {profile}"}), 200
    return jsonify({"error": "Invalid token or profile"}), 400

if __name__ == '__main__':
    app.run(port=5000)
