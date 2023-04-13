from twilio.twiml.messaging_response import MessagingResponse
from api.gpt4 import generate_response


def create_twilio_response(response_text):
    twilio_response = MessagingResponse()
    twilio_response.message(response_text)
    return str(twilio_response)
