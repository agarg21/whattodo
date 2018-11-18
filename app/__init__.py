import os
from flask import Flask, request
from twilio.rest import Client
from twilio.twiml.messaging_response import Message, MessagingResponse

# Initialize application
app = Flask(__name__)


account_sid = "AC295f2f41a6f1ba5e8c8450536b773693"
auth_token = "7a5edf40bd20ed732fb664594ef5a31a"


client = Client(account_sid, auth_token)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/incoming', methods=['POST'])
def incoming():
    app.logger.info('Request form %s', request.form)
    print ('Request form %s', request.form)

    message_body = request.form['Body']
    resp = MessagingResponse()

    reply_text = message_body
    resp.message('Hi\n\n' + reply_text)
    return str(resp)