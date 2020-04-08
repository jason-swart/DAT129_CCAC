#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 18:00:07 2020

Scraping demo for DAT-129

    Goodread.com scraping

    QUESTION: 
    Before scraping the page, check:
        1) Are the URLs encoded in a sensible way that we can use
        the urllib to grab the HTML page easily?
        2) Are the elements on the page that we want to scrape enclosed
        in HTML tabs with distinctive class names or tag names?

@author: kynligbein
"""

import urllib
from bs4 import BeautifulSoup

def getSearchURL(term):
    # Assembles a query against the website URL given a search term
    url = "https://www.goodreads.com/search?q=%s&search_type=books" % (str(term))
    return url


def getPageText(url):
#    Given a URL, fetches the raw HTML from the internet
#   build the request object fromt he given URL
    req = urllib.request.Request(url)
    # access the network via standard gateway
    # to actually retrieve the HTML from goodreads.com server
    with urllib.request.urlopen(req) as response:
        return response.read()

term = "virus"
url = getSearchURL(term)
print(url)
pageText = getPageText(url)
# Pass raw HTML and name of desired parser
soup = BeautifulSoup(pageText, 'html.parser')
# Extract components with specific calls through soup
bookatags = soup.find_all('a', 'bookTitle')
totalTitles = 0
subTitles = 0
# The bookatags is iterable and contains all the mini-trees whose parent
# is an <a> tag of class bookTitle
for book in bookatags:
    title = book.find('span').string
    print(title)
    totalTitles += 1
    if ":" in title:
        subTitles += 1
        
print("Total titles: ", str(totalTitles))
subts = (subTitles/totalTitles)*100
print(str(subts), "% of books have subtitles.")
