from flask import Flask
import socket
import os

app = Flask(__name__)

@app.route('/hello')
def hello1234():
    print("Hello World")
    return "<p>Hello, World!</p>"

if __name__ == "main":
    app.run(hostname='0.0.0.0',port=80)