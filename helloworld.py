'''
Created on Feb 15, 2015

@author: Rebecca
'''

import os
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/sharon')
def truth():
    return "She's kind of the best"

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)