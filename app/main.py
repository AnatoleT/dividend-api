from flask import Flask
from flask import request
from bs4 import BeautifulSoup
import json
import requests

app = Flask(__name__)

#Give the amount of dividend based on the ticker
@app.route("/stock/dividend/amount")
def amountDividend():
	page = request.args.get('ticker', default = "goog", type = str)
	session = requests.Session()
	my_headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36", 
          "Accept":"text/html,application/xhtml+xml,application/xml; q=0.9,image/webp,image/apng,*/*;q=0.8"}
	url = 'https://finviz.com/quote.ashx?t=' + page
	response = session.get(url, headers=my_headers)
	soup = BeautifulSoup(response.text, 'html.parser')
	tab = soup.find("table",{"class":"snapshot-table2"})
	td = tab.find_all("td")
	for i in range (len(td)):
		if td[i].text == "Dividend":
			nthDividend = td[i + 1]
			dividendAmount = nthDividend.find("b").text
			json = '{ "Request":"Dividend", "amount":' + dividendAmount + '}'
			return json

#Give the price of the stock based on the ticker
@app.route("/stock/price")
def price():
	page = request.args.get('ticker', default = "goog", type = str)
	session = requests.Session()
	my_headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36", 
          "Accept":"text/html,application/xhtml+xml,application/xml; q=0.9,image/webp,image/apng,*/*;q=0.8"}
	url = 'https://finviz.com/quote.ashx?t=' + page
	response = session.get(url, headers=my_headers)
	soup = BeautifulSoup(response.text, 'html.parser')
	tab = soup.find("table",{"class":"snapshot-table2"})
	td = tab.find_all("td")
	for i in range (len(td)):
		if td[i].text == "Price":
			nthPrice = td[i + 1]
			price = nthPrice.find("b").text
			json = '{ "Request":"Price", "Price":' + price + '}'
			return json

#Give the market capitalisation of the stock based on the ticker
@app.route("/stock/marketcap")
def price():
	ticker = request.args.get('ticker', default = "goog", type = str)
	session = requests.Session()
	my_headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36", 
          "Accept":"text/html,application/xhtml+xml,application/xml; q=0.9,image/webp,image/apng,*/*;q=0.8"}
	url = 'https://finviz.com/quote.ashx?t=' + ticker
	response = session.get(url, headers=my_headers)
	soup = BeautifulSoup(response.text, 'html.parser')
	tab = soup.find("table",{"class":"snapshot-table2"})
	td = tab.find_all("td")
	for i in range (len(td)):
		if td[i].text == "Market Cap":
			nthMarketCap = td[i + 1]
			marketCap = nthMarketCap.find("b").text
			json = '{ "Request":"Market Cap", "Price":' + marketCap + '}'
			return json