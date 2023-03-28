from flask import Flask
from model import run_model

app = Flask(__name__)

@app.route("/")
def hello_world():
    results = run_model("Bullet to the Head")
    return f"<p>{results}</p>"