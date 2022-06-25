from flask import Flask
import json
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route("/")
def home_view():
	data_set = {"Page" : "Home", "Message" : "Hello World"}
	json_dump = json.dumps(data_set)
	return json_dump