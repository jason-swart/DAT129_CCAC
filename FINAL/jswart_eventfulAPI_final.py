#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  5 17:58:30 2020

@author: kynligbein
"""

import requests, json, csv, eventful
import pandas as pd

# During initial testing of this script, API documentation recommended using a 
# pre-designed script containing objects to assist pulling data from the Eventful
# API. However, it calls many methods no longer used, specifically for 'urllib'.
# Creating a 'url' variable and hand-crafting the query to include the auth-key 
# proved more effective than cleaning the eventful.py call. I left it imported 
# however on the grounds that the script and its objects can be cleaned for use.

# Query includes a list of 50 (Eventful allows for a maximum of 250) venues sorted
# by popularity. Further parameters could be used to sort by genre and/or venue type.

url = 'http://api.eventful.com/json/venues/search?app_key=DbR3FqcwWwDM2KGL&include=categories&page_size=50&sort_order=popularity&location=Pittsburgh'
req = requests.get(url)
if(int(req.status_code) == 200):
    
# Printing req.headers.keys() would show the keys as well as the arrays located
# in the value associated with the "venues" key.
    
# Creating a variable for the JSON, containing the request .text info, but only 
# if the requests status_code returns with a good "200" code.
    
    apiDict = json.loads(req.text)
#    print(apiDict)

# Using pandas to create a dataframe of the JSON arrays found in the key 'venues'
# then generate a CSV with the arrays.
    
df = pd.DataFrame(apiDict['venues'])
df.to_csv('venues.csv', index = False)