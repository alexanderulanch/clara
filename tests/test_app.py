from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)


@app.route("/sms", methods=["POST"])
def sms_reply():
    return "Hello from Test App!"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
