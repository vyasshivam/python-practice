# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 13:11:40 2017

@author: User
"""

import requests
from bs4 import BeautifulSoup

def getTitles() :
    _url = input('Enter url : ')
    className = input('Enter class name : ')
    r = requests.get(_url)
    soup = BeautifulSoup(r.content)
        
    for story_heading in soup.find_all(class_= className):    
        if story_heading.a: 
            print(story_heading.a.text.replace("\n", " ").strip())
        else: 
            print(story_heading.contents[0].strip())

getTitles()        