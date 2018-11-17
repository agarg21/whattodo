import os
from flask import Flask

# Initialize application
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
