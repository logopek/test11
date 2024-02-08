from flask import Flask, request
import json
app = Flask(__name__)
text_to_return = "Hi!"
@app.route("/")
def hello_world():
    return text_to_return

@app.route("/newMsg", methods = ["POST"])
def newMsg():
    print(request)
    global text_to_return
    x = json.loads(request.json)
    text_to_return = x["text"]
app.run(host="0.0.0.0",port = 8190)
