from flask import Flask, request, make_response
import json
app = Flask(__name__)
text_to_return = "Hi!"
@app.route("/")
def hello_world():
    s = "Hello!"
    response = make_response(s)
    response.headers.add('content-length', str(len(s.encode('utf-8'))))
    return response

@app.route("/newMsg", methods = ["POST"])
def newMsg():
    print(request.data)
    return "0"


app.run(host="0.0.0.0",port = 8190)
