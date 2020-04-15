#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 09:36:56 2020

@author: kynligbein
"""

from urllib.request import urlopen as uReq # "as" can be anything I want
from bs4 import BeautifulSoup as Soup # again, "as" can be anything

searchURL = "https://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card" #enter URL to scrape


scraper = uReq(searchURL)

page_soup = Soup(scraper.read(), "html.parser")
scraper.close()
#print(page_soup.body.span) #grabs and prints first span tag in the body

itemCont = page_soup.find_all('div', {"class" : "item-container"})

outFile = "graphics_cards.csv"
headers = "brand, product_name, shipping \n"

f = open(outFile, "w")
f.write(headers)

for containers in itemCont:
    ratingSP = containers.div.select('a')
    
    brand = ratingSP[0].img['title'].title()
    
    prodName = containers.div.select('a')[2].text
    
    shipping = containers.find_all('li', {'class' : 'price-ship'})[0].text.strip().replace('$', "").replace(' Shipping', "")

    print("Brand: ", + brand + "\n")
    print("Product_Name: " + prodName + "\n")
    print("Shipping: " + shipping + "\n")

    f.write(brand + ", " + prodName.replace(",", "|") + ", " + shipping + "\n")
    
f.close()

