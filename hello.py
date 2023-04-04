from flask import request
from model import run_model
import json

app = Flask(__name__)

@app.route('/') 
def index(): 
    return "Flask server" 

@app.route("/entermovietitle", methods=['POST'])
def hello_world():
    data = request.get_json()
    results = run_model(data['title'])
    #print(results)
    return results

if __name__ == "__main__": 
	app.run(host = "0.0.0.0", port = 5000, debug = True) 