from flask import Flask,jsonify

app = Flask(__name__)

# Returns device hostname,IP and MAC address
@app.route("/details")
def details():
    hostname,ip,mac = get_device_details()
    out = "Hello!!!....I'm " + hostname + "....My MAC ID is " + mac + "....and My IP address is "+ip
    return out

@app.route("/health")
def health():
    return jsonify(
        status="up"
    )

@app.route("/")
def basic():
    return "Hello from DevOps Made Easy"

@app.route("/configmap")
def configmap():
    app.config.from_pyfile('/config/config.cfg')
    return app.config['MSG']

if __name__ == "__main__":
    app.run(port=5000, debug=True)
