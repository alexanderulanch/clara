import os
from twilio.rest import Client

# Get Twilio credentials and phone numbers from environment variables
account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]
to_phone_number = os.environ["MY_PHONE_NUMBER"]
from_phone_number = os.environ["TWILIO_PHONE_NUMBER"]

# Create a Twilio client
client = Client(account_sid, auth_token)

# Define the message content
message_body = "Hello, this is a test message from Twilio!"

# Send the SMS message
message = client.messages.create(
    body=message_body, from_=from_phone_number, to=to_phone_number
)

# Print the message SID
print(f"Message SID: {message.sid}")
