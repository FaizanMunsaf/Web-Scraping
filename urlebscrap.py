# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 12:03:29 2022

@author: Faizan
"""

#import the library used to query a website
import urllib2

#specify the url you want to query
url = "http://www.python.org"

#Query the website and return the html to the variable 'page'
page = urllib2.urlopen(url)

#import the Beautiful soup functions to parse the data returned from the website
from BeautifulSoup import BeautifulSoup

#Parse the html in the 'page' variable, and store it in Beautiful Soup format
soup = BeautifulSoup(page)

#to print the soup.head is the head tag and soup.head.title is the title tag
print(soup.head)
print(soup.head.title)

#to print the length of the page, use the len function
print(len(page))

#create a new variable to store the data you want to find.
tags = soup.findAll('a')

#to print all the links
print(tags)

#to get all titles and print the contents of each title
titles = soup.findAll('span', attrs = { 'class' : 'titletext' })
for title in titles:
    print(title.contents)