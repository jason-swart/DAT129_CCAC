#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 12:07:02 2020

@author: kynligbein
"""

import csv


def processJailCSV():
    '''
        Iterates over Allegheny county jail census data to tabulate
        inmates by race: To what degree does the inmate population by
        race reflect the composition of the county?
    
        retrieved from WRPDC on 12-FEB-2020 via
        https://data.wprdc.org/dataset/allegheny-county-jail-daily-census
    '''
#Switched to a "with open" command to open and close the csv file.
    with open('acj_june2019.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        raceCount = {'B':0, 'W':0}
        focusDate = '2019-06-01'
        
        for row in reader:
            if row['Date'] == focusDate:
                if row['Race'] == 'B':
                    raceCount['B'] = raceCount['B'] + 1
                elif row['Race'] == 'W':
                    raceCount['W'] = raceCount['W'] + 1
                
    return raceCount

processJailCSV()

def computePercents(raceDict):
    total = 0
    for k in raceDict:
        total = total + raceDict[k]
    for k in raceDict:
        perc = raceDict[k] / total
        print("Frac of inmates " + k + ": " + str(perc))

d = processJailCSV()
computePercents(d)