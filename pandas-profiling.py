# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 21:37:05 2020

@author: anukriti
"""
import numpy as np
import pandas as pd
from pandas_profiling import ProfileReport  

df= pd.read_csv('datasets/phishcoop.csv')

### To Create the Simple report quickly
profile = ProfileReport(df, title='Pandas Profiling Report', explorative=True)

profile.to_widgets()

profile.to_file("output.html")
