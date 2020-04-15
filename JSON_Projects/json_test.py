#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 19:45:29 2020

@author: kynligbein
"""
import json

#sample read in and out of JSON to and from text file.
with open('capital_projects.json') as jsontest:
    capprojkeywords = json.load(jsontest)
#    print(capprojkeywords)
    print(capprojkeywords['fiscal_year'])