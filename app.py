from flask import Flask
import socket
import os

app = Flask(__name__)

@app.route('/hello')
def hello():
    print("Hello World")
    return html.format(name=os.getenv("NAME", "world"), hostname=socket.gethostname())

if __name__ == "main":
    app.run(hostname='0.0.0.0',port=80)