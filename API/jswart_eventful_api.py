#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 18:47:20 2020

@author: kynligbein
"""

import requests, json, eventful 

req = requests.get('http://api.eventful.com/json/venues/search?app_key=DbR3FqcwWwDM2KGL&include=categories&location=Pittsburgh')
if(int(req.status_code) == 200):
#     print(req.headers.keys())
    apiDict = json.loads(req.text)
    print(apiDict)
