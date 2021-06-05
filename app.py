from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse
from notion.client import NotionClient
app = Flask(__name__)

def notionConnect():
    client = NotionClient(token_v2="108f91fb55af7f8f944bae8d3a5db8adbf55f4c43e81227e92beae5f83aadaa7b8663da0dee2b417bd20d665f87852cb672d5adcf003b4930656899f22f0a32c294cd0ca8072235e549df37b4fc6")
    page = client.get_collection_view("https://www.notion.so/a2ba916475ab4760a6e382d2edaa0674?v=5454c4fc1cb140eb8c573a3921ecc2bf")
    return page 


@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()    
    page = notionConnect()
    ct = 0 
    for obj in page.collection.get_rows():
        print(obj.title)
        ct+=1

    responded = False
    if 'hello' in incoming_msg:
        msg.body("There are "+ct+" puzzles available")
        responded = True
    if 'bye' in incoming_msg:
        msg.body("Sayonara")
        responded = True
    if not responded:
        msg.body('I sorry!')
    return str(resp)


if __name__ == '__main__':
    app.run()