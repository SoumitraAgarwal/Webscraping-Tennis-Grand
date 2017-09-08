# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import os
import urllib2
import requests
import pandas as pd

os.mkdir("Pictures")
data = pd.read_csv("Names.csv")
url = "http://www.tennis.com"

proxies = {
  'http': 'http://172.16.114.112:3128',
  'https': 'https://172.16.114.112:3128',
}

for i in range(len(data)):
	print("Working for " + data["Name"][i])

	temp_url = url + data["url"][i]
	page = requests.get(temp_url,proxies=proxies)

	html = page.content
	soup = BeautifulSoup(html,'lxml')
	Nat	 = soup.find('div', class_='player-image')
	print(Nat['data-image'])
	while(True):
		try:
			response = requests.get(Nat['data-image'], stream=True,proxies=proxies)
		except requests.exceptions.RequestException as e:  # This is the correct syntax
			print(e)
			continue
		break
		
	with open('Pictures/'+ data['Name'][i]+'.png', 'wb') as out_file:
		shutil.copyfileobj(response.raw, out_file)
	del response