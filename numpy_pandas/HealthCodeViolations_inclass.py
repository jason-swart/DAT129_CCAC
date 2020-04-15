# -*- coding: utf-8 -*-
"""
Spyder Editor

In-class demonstration of numpy and pandas

This is a temporary script file.
"""

import numpy as np
import pandas as pd

# Sample script for accessing and slicing a CSV based dataset with pandas

violationsDF = pd.read_csv('foodinspectionviolations_alghcnty.csv')
#print(type(violationsDF))
#print(violationsDF.head())
#print(violationsDF.dtypes)

codeviolations = violationsDF['description_new']
#print(type(codeviolations))
#print(codeviolations.size)
#print(codeviolations.value_counts())

munis = violationsDF['municipal']
#print(munis.value_counts())

#print(violationsDF.iloc[0:10])

robviols = violationsDF.loc[lambda violationsDF: violationsDF['municipal'].isin(['Robinson'])]

#print(robviols['description_new'].value_counts())