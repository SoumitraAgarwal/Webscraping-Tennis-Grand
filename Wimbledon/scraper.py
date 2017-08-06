# -*- coding: utf-8 -*-
import urllib2
import requests
import dryscrape
import pandas as pd
from bs4 import BeautifulSoup

years = range(2001,2017)
url = "http://www.scoreboard.com/en/tennis/atp-singles/wimbledon-2001/results/"
proxies = {
  'http': 'http://172.16.114.112:3128',
  'https': 'https://172.16.114.112:3128',
}
session = dryscrape.Session()	
session.set_proxy(host='172.16.114.112',port = 3128)
session.visit(url)
response = session.body()
soup = BeautifulSoup(response, "lxml")

data = soup.find('table', class_='tennis')
text = []

for row in data:
	f = open('table.txt', 'a+')
	f.write(str(row) + "\n")
	f.close()