#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 18:03:11 2020

@author: kynligbein
"""

from zipfile import ZipFile
import os
import re

with ZipFile('Books_expandedByNia1302.zip', 'r') as zipObj:
    zipObj.extractall()

# Alternate zip file that could be extracted to test script on; just needs to 
# have it uncommented.

#with ZipFile('fileTree_Board Games_Mellisha_1380382.zip', 'r') as zipObj:
#    zipObj.extractall()

regexp = re.compile('(\.\w+)$')

def interrogateFiles(dirname, filelist):
    ''' 
    take in a directory name and its contents and contents files and count files
    with .jpg extension
    '''
    for file in filelist:
        fn = dirname + str(os.sep) + file
        print('file name: ', fn )
        if os.path.isfile(fn):
            print('File size: ', end = '')
            print(os.path.getsize(fn), 'B')
            match = re.search(regexp, fn)
            if match:
                print('Extension: ', match.group(0))

def traverse(walkroot):
    for loc, dir, files in os.walk(walkroot):
        print(loc, ' ', dir, ' ', files)
        interrogateFiles(loc, files)
        
traverse('.')