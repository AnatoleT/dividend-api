from flask import Flask
from bs4 import BeautifulSoup
import json
import requests

app = Flask(__name__)

@app.route("/")
def home_view():
	session = requests.Session()
	my_headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36", 
          "Accept":"text/html,application/xhtml+xml,application/xml; q=0.9,image/webp,image/apng,*/*;q=0.8"}
	url = 'https://finviz.com/quote.ashx?t=TTE'
	response = session.get(url, headers=my_headers)
	soup = BeautifulSoup(response.text, 'html.parser')
	tab = soup.find("table",{"class":"snapshot-table2"})
	data_set = {"Page" : "Home", "Message" : "Hello World"}
	td = tab.find_all("td")
	for i in range (len(td)):
		if td[i].text == "Dividend":
			nthDividend = td[i + 1]
			dividendAmount = nthDividend.find("b")
			return "<h1>" + dividendAmount.text + "</h1>"