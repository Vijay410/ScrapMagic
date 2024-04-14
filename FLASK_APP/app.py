from flask import Flask
import os

app = Flask(__name__)


from controler import *

if __name__ == '__main__':
    app.run(debug=True)
