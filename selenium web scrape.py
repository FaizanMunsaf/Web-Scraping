# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 10:36:19 2022

@author: Faizan
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


# =============================================================================
# Disable chrome items
# =============================================================================
options = Options()
prefs = {"profile.default_content_setting_values.notifications" : 2}
options.add_experimental_option("prefs",prefs)
options.add_experimental_option("excludeSwitches", ["disable-popup-blocking"])
options.add_experimental_option("useAutomationExtension", False)
options.add_experimental_option("excludeSwitches",["enable-automation"])
#options.add_argument("--incognito")
path =  r'C:\Users\Faizan\.wdm\drivers\chromedriver\win32\106.0.5249\chromedriver.exe'
# Here Chrome will be used
driver = webdriver.Chrome(service=Service(path),options=options)
# =============================================================================
# End items
# =============================================================================

driver.get("https://www.youtube.com/")

# with div tag
wikipedia = driver.find_elements(By.TAG_NAME, value="div")

f = open("wikipeida.txt","w")
for wiki_list in wikipedia:
    f.write(str(wiki_list.text.encode("utf-8"))+"\n")
f.close()
    

# with p tag
wikipedia = driver.find_elements(By.TAG_NAME, value="p")

f = open("wikipeida_1.txt","w")

for wiki_list in wikipedia:
    f.write(str(wiki_list.text.encode("utf-8"))+"\n")

f.close()


# with a tag
wikipedia = driver.find_elements(By.TAG_NAME, value="a")

f = open("wikipeida_2.txt","a")

for wiki_list in wikipedia:
     print(str(wiki_list.text)+"\n")
    
f.close()
    
    
    
    
    
    
    
    
    
    