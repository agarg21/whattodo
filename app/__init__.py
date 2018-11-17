import os
from flask import Flask, request

# Initialize application
app = Flask(__name__)


accountSid = "AC295f2f41a6f1ba5e8c8450536b773693"
authToken = "7a5edf40bd20ed732fb664594ef5a31a"

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/incoming', methods=['POST'])
def incoming():
    app.logger.info('Request values %s', request.values)
    app.logger.info('Request data %s', request.data)
    app.logger.info('Request headers %s', request.headers)
    print ('Request values %s', request.values)
    print('Request data %s', request.data)
    print('Request headers %s', request.headers)
    return "All good!"