from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from api.gpt4 import generate_response

app = Flask(__name__)

conversation_history = []


@app.route("/sms", methods=["POST"])
def sms_reply():
    global conversation_history

    incoming_message = request.form.get("Body")
    conversation_history.append(("user", incoming_message))

    gpt4_response = generate_response(conversation_history)
    conversation_history.append(("assistant", gpt4_response))

    twilio_response = MessagingResponse()
    twilio_response.message(gpt4_response)
    return str(twilio_response)


if __name__ == "__main__":
    app.run(debug=True)
