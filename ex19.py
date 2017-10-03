# -*- coding: utf-8 -*-
"""
Using the requests and BeautifulSoup Python libraries, print to the screen the full text of the article 
on this website: http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture.

The article is long, so it is split up between 4 pages. Your task is to print out the text to the screen 
so that you can read the full article without having to click any buttons.
"""

import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":

	r=requests.get("http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture")
	
	soup=BeautifulSoup(r.text,"html.parser")

	for a in soup.find_all(class_="content-section"):
		for b in a.find_all("p"):
			print(b.text)