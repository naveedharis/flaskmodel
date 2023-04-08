from flask import Flask, request
from model import run_model

app = Flask(__name__)

#@app.route('/') 
#def index(): 
#    return "Flask server" 

#@app.route("/entermovietitle", methods=['POST'])
@app.route("/", methods=['POST'])
def recommend_movie():
    data = request.get_json()
    results = run_model(data['title'])
    return results
