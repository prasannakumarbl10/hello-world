from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return("Hello world from kubernetes!")

app.run(host="0.0.0.0", port=5000) 
