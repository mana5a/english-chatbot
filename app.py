from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse
from notion.client import NotionClient
app = Flask(__name__)

def notionConnect():
    client = NotionClient(token_v2="108f91fb55af7f8f944bae8d3a5db8adbf55f4c43e81227e92beae5f83aadaa7b8663da0dee2b417bd20d665f87852cb672d5adcf003b4930656899f22f0a32c294cd0ca8072235e549df37b4fc6")
    page = client.get_block("https://www.notion.so/4c884665930e48d3bd2e76d4ff13084c?v=9bb58e513a554446b7b0e7e9b4d74f17")
    return page 


@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()    
    page = notionConnect()
    for child in page.children:
        response = child.title

    responded = False
    if 'hello' in incoming_msg:
        msg.body("This is "+response)
        responded = True
    if 'bye' in incoming_msg:
        msg.body("Sayonara")
        responded = True
    if not responded:
        msg.body('I sorry!')
    return str(resp)


if __name__ == '__main__':
    app.run()