from flask import Flask, request
from model import run_model

app = Flask(__name__)

#@app.route('/') 
#def index(): 
#    return "Flask server" 

#@app.route("/entermovietitle", methods=['POST'])
@app.route("/", methods=['GET','POST'])
def recommend_movie():
    data = request.get_json()
    print(data)
    results = run_model(data['movieId'],data['title'])
    return results
