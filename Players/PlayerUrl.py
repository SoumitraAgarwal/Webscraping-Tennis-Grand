# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib2
import requests
import pandas as pd

url = "http://www.tennis.com/rankings/ATP/"
proxies = {
  'http': 'http://172.16.114.112:3128',
  'https': 'https://172.16.114.112:3128',
}

page = requests.get(url,proxies=proxies)

html = page.content
soup = BeautifulSoup(html,'lxml')
right_table=soup.find('table', class_='tennis-table')

URL = []
Player = []
iterator = 0

for row in right_table.findAll("tr", class_ = 'player-row'):
    cells = row.find("td", class_ = 'player-name')
    if(cells!=None):
    	a = cells.find("a")
    	if(a!=None):
	    	URL.append(a["href"])
	        Player.append(a.find(text = True))
	        iterator += 1

	print("Done for " + Player[iterator])
	df=pd.DataFrame({'Name':Player, 'url' : URL})
	print(df)
	df.to_csv('Names.csv', index = False, encoding = 'utf-8')

