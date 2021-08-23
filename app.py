from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World! Team 3 is best :P"
    return "hope this doesnt change everyones"
