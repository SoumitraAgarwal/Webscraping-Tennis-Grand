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
# text = data.find(text = True)
print(data)
	
# driver.get(url,proxies=proxies)

# This will get the initial html - before javascript
# html1 = driver.page_source

# This will get the html after on-load javascript
# html2 = driver.execute_script("return document.documentElement.innerHTML;")
# print(html2)
# A=[]
# B=[]

# for row in right_table.findAll("tr"):
#     cells = row.find("td")
#     if(cells!=None):
#     	a = cells.find("a")
#     	if(a!=None):
# 	    	A.append(a["title"])
# 	        B.append(a["href"])

# temp_df=pd.DataFrame({'Name':A, 'url' : B})
# print(temp_df)

# for i in range(2,588):
# 	print(i)
# 	url_temp = url+'/players/'+str(i)+'/'
	
# 	while(True):
# 		print("Getting page "+str(i))
# 		try:
# 			page = requests.get(url_temp,proxies=proxies)
# 		except requests.exceptions.RequestException as e:  # This is the correct syntax
# 			print(e)
# 			continue
# 		break

# 	html = page.content
# 	soup = BeautifulSoup(html,'lxml')
# 	right_table=soup.find('table', class_='table table-striped players')

# 	for row in right_table.findAll("tr"):
# 	    cells = row.find("td")
# 	    if(cells!=None):
# 	    	a = cells.find("a")
# 	    	if(a!=None):
# 		    	A.append(a["title"])
# 		        B.append(a["href"])
# 	df=pd.DataFrame({'Name':A, 'url' : B})
# 	print(df)
# df.to_csv('Names.csv', index = False, encoding = 'utf-8')

