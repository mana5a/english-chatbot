from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)


@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    if 'hello' in incoming_msg:
        msg.body("it's me :D")
        responded = True
    if 'bye' in incoming_msg:
        msg.body("Sayonara")
        responded = True
    if not responded:
        msg.body('I sorry!')
    return str(resp)


if __name__ == '__main__':
    app.run()