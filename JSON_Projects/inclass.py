#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 18:56:22 2020

@author: kynligbein
"""
import json

##sample read in and out of JSON to and from text file.
#with open('gitinfo.json') as jsontest:
#    gitkeywords = json.load(jsontest)
##    print(gitkeywords)
#    print(gitkeywords['Remotes'][1])
#    
#encode python object as JSON and write to a file
projects = {}
projects["group1"] = ['Dan', 'Eric', 'Eric1', 'Eric2', 'Eric3']
projects["group2"] = ('Zach', 'Taichi', 'Joel')
projects["unallocated"] = 452
#print(projects)
with open('groups.json', 'w') as groupfile:
    #arg1 is the object to serialize, arg2 is the file
    json.dump(projects, groupfile)
 
#projareas = []

# with open('proj', 'r') as projs:
#    for p in projs
#       if p["area"] ==
#            logMalformedProject(p)
#       if p[area] not in projareas
#
    
#def logMalformedProject:
#    with open('malproj.txt', 'a') as log:
    #write proj ID to file