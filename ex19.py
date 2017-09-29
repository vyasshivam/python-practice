# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 16:46:36 2017

@author: User
"""

import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":

	r=requests.get("http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture")
	
	soup=BeautifulSoup(r.text,"html.parser")

	for a in soup.find_all(class_="content-section"):
		for b in a.find_all("p"):
			print(b.text)