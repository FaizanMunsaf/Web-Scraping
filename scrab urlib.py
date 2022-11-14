# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 10:36:07 2022

@author: Faizan
"""

# Accessing website conent from web page

import requests
URL = "https://www.geeksforgeeks.org/data-structures/"
r = requests.get(URL)
print(r.content)

f = open("urlibscab.txt","w")
f.write(str(r.content))
f.close()

# Accessing website content through Agent

headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"}
# Here the user agent is for Edge browser on windows 10. You can find your browser user agent from the above given link.
r = requests.get(url=URL, headers=headers)
f = open("agent.txt","w")
f.write(str(r.content))
f.close()