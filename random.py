from flask import Flask
import random

app = Flask(__name__)

# ランダムに表示する文字列
sentences = [
    "<p>Hello World!<p>",
    "<p>こんにちは 世界!<p>",
    "<p>Hallo Welt<p>",
    "<p>Bonjour le monde<p>"
]

@app.route("/")
def hello_world():
    sentence = random.choice(sentences) # ランダム表示
    return sentence