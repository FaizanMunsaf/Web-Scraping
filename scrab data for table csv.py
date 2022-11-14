# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 11:45:25 2022

@author: Faizan
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

soup = BeautifulSoup(urlopen('https://www.hubertiming.com/results/2018MLK'))
data = []

for row in soup.select('#individualResults tr:has(td)'):
    row_list = row.find_all("td")
    dataRow = []
    for cell in row_list:
        dataRow.append(cell.text.strip())
    data.append(dataRow)
    
pd.DataFrame(data, columns=[h.text for h in soup.select('#individualResults th')])