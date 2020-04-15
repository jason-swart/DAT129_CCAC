#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 14:37:48 2020

@author: kynligbein
"""

import numpy as np
import pandas as pd

# Script for accessing and slicing a CSV based dataset with pandas

violationsDF = pd.read_csv('foodinspectionviolations_alghcnty.csv')

# Creates a variable for listing violations from the sliced dataset under the 
# CSV column heading "description_new"

codeviolations = violationsDF['description_new']

# Creates a variable to list the items under the "municipal" column heading

munis = violationsDF['municipal']

# Creates a variable for each of three chosen municipalities then uses lambda 
# function to sort the violations for each location

millviols = violationsDF.loc[lambda violationsDF: violationsDF['municipal'] == 'Millvale']
rossviols = violationsDF.loc[lambda violationsDF: violationsDF['municipal'] == 'Ross']
bellviols = violationsDF.loc[lambda violationsDF: violationsDF['municipal'] == 'Bellevue']

# Create variables to search for the health violation with the most "high" rated
# severity

highVio = violationsDF.loc[lambda violationsdf: violationsDF['high']=='T']
vioList = highVio['description_new'].value_counts()

# Creates new variables that lists number of violations for each location using 
# value_counts then using nlargest pulls the top 3 violations for each location

Millvale = millviols['description_new'].value_counts().nlargest(3)
Ross = rossviols['description_new'].value_counts().nlargest(3)
Bellevue = bellviols['description_new'].value_counts().nlargest(3)

print("Millvale: \n", Millvale, "\n", sep='')
print("Ross: \n", Ross, "\n", sep='')
print("Bellevue: \n", Bellevue, "\n", sep='')

print("Violation with the most 'high' severity rating is: ")
print(vioList.head(1))
