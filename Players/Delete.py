# -*- coding: utf-8 -*-
import os
import cv2
import pandas as pd
import requests
from bs4 import BeautifulSoup
import shutil

base = 'Pictures1/'
a = os.listdir(base)
incorrect = [];

for i in range(len(a)):
    im = cv2.imread(base+a[i])
    if(im is None):
    	incorrect.append(a[i])

for i in range(len(incorrect)):
	print(i)
	print("Removing "+ base+incorrect[i])
	os.remove(base+incorrect[i])
