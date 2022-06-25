from flask import Flask
from bs4 import BeautifulSoup
app = Flask(__name__)

@app.route("/")
def home_view():
	return "Bienvenue Anat"
