# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import os
import requests
import shutil

if("Pictures1" not in os.listdir(".")):
	os.mkdir("Pictures1")

proxies = {
  'http': 'http://172.16.114.19:3128',
  'https': 'https://172.16.114.19:3128',
}

url 	= "http://www.atpworldtour.com"
page 	= open("scrape.html")
soup 	= BeautifulSoup(page.read(), "lxml")

avatars = soup.findAll('td', class_="player-avatar-cell")
names	= soup.findAll('td', class_="player-cell")

iterat  = 0

for avatar in avatars:
	Nat 	= avatar.find('img')
	rank	= soup.find('td', class_= "rank-cell")
	rank 	= int(rank.find(text=True))
	name 	= names[iterat].find(text = True)
	iterat += 1

	print("Working for " + name + " " + str(iterat))
	
	for i in range((103-rank)/2):
		while(True):
			try:
				response = requests.get(url+Nat['src'], stream=True,proxies=proxies)
			except requests.exceptions.RequestException as e:  # This is the correct syntax
				print(e)
				continue
			break	
		with open('Pictures1/'+ name + str(i) + '.png', 'wb') as out_file:
			shutil.copyfileobj(response.raw, out_file)
		del response