#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 18:50:44 2020

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

term = "horror"
url = getSearchURL(term)
#print(url)
pageText = getPageText(url)

soup = BeautifulSoup(pageText, 'html.parser')

bookaTags = soup.find_all('a', {'class': ['bookTitle', 'authorName']})

for book in bookaTags:
    bookList = book.find('span').string
    print(bookList)

#bookTitle = soup.find_all('a', 'bookTitle')
#bookAuthor = soup.find_all('a', 'authorName')
#
#for book in bookTitle:
#    title = book.find('span').string
#    print(title)
#
#for name in bookAuthor:
#    name = name.find('span').string
#    print(name)