from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return """Настя лошара
    <a style="display:none" href="https://github.com/logopek/test11">Правильно мыслишь)</a>
    """

@app.route("/love")
def love():
    return "Конечно, это все шутки, Настя лучшая!"
app.run(host="0.0.0.0",port = 443)
