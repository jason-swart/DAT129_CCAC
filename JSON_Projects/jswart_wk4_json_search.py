#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 20:01:55 2020

@author: kynligbein
"""

import json, csv

def processCapProjCSV():
    with open('capital_projects.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        