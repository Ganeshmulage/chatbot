# app.py
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(force=True)
    action = req.get('queryResult').get('action')
    
    if action == 'authenticate':
        return authenticate(req)
    elif action == 'get_journey_details':
        return get_journey_details(req)
    elif action == 'select_train':
        return select_train(req)
    elif action == 'collect_passenger_details':
        return collect_passenger_details(req)
    elif action == 'confirm_details':
        return confirm_details(req)
    elif action == 'process_payment':
        return process_payment(req)
    else:
        return jsonify({'fulfillmentText': 'I did not understand that action.'})

def authenticate(req):
    # Mock authentication
    credentials = req['queryResult']['parameters']
    username = credentials.get('username')
    password = credentials.get('password')
    
    if username == 'user' and password == 'pass':
        return jsonify({'fulfillmentText': 'Authentication successful. Please provide the journey details.'})
    else:
        return jsonify({'fulfillmentText': 'Authentication failed. Please check your credentials and try again.'})

def get_journey_details(req):
    # Mock journey details handling
    return jsonify({'fulfillmentText': 'Journey details received. Please select a train from the available options.'})

def select_train(req):
    # Mock train selection
    return jsonify({'fulfillmentText': 'Train selected. Please provide passenger details.'})

def collect_passenger_details(req):
    # Mock passenger details collection
    return jsonify({'fulfillmentText': 'Passenger details collected. Please review and confirm your booking.'})

def confirm_details(req):
    # Mock confirmation
    return jsonify({'fulfillmentText': 'Details confirmed. Proceeding to payment.'})

def process_payment(req):
    # Mock payment processing
    return jsonify({'fulfillmentText': 'Payment successful. Your booking is confirmed. PNR: XYZ123'})

if __name__ == '__main__':
    app.run(port=5000, debug=True)
