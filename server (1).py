import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from twilio.rest import Client
from dotenv import load_dotenv

# 1. Load environment variables specifically from your key.env file
load_dotenv('key.env')

app = Flask(__name__)
CORS(app) # Allow the HTML frontend to communicate with this server

# 2. Grab credentials from the environment variables
account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
twilio_phone = os.environ.get('TWILIO_PHONE')
your_phone = os.environ.get('YOUR_PHONE')

# Initialize Twilio Client
client = Client(account_sid, auth_token)

# 3. Create the route that the frontend will call
@app.route('/send-alert', methods=['POST'])
def send_alert():
    data = request.get_json()
    message_body = data.get('message', 'Emergency threshold exceeded.')

    try:
        # Send the SMS using Twilio
        message = client.messages.create(
            body=f"HYDRO-SENSE ALERT: {message_body}",
            from_=twilio_phone, # Note: Twilio Python uses 'from_' because 'from' is a reserved word
            to=your_phone
        )
        return jsonify({'success': True, 'sid': message.sid}), 200
    
    except Exception as e:
        print(f"Error sending SMS: {e}")
        return jsonify({'success': False, 'error': str(e)}), 500

if __name__ == '__main__':
    # Run on port 3000 to match the frontend fetch request
    print("Starting HydroSense Python Alert Server on port 3000...")
    app.run(port=3000, debug=True)