# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 00:33:40 2019

@author: Zia-ur-Rehman Khan
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas import datetime
def parser(x):
	return datetime.strptime('190'+x, '%Y-%m')
df=pd.read_csv('C:\\Users\\Zia-ur-Rehman Khan\\Desktop\\roundhack\\hack.csv', header=0, parse_dates=[0], index_col=0, squeeze=True, date_parser=parser)
#print(dataset)
#Subsetting the dataset
#Index 11856 marks the end of year 2013


#Creating train and test set 
#Index 10392 marks the end of October 2013 
train=df[0:215106] 
test=df[215106:]

#Aggregating the dataset at daily level
#df.Timestamp = pd.to_datetime(df['Donation_Date'],format='%d-%m-%Y') 
df.Timestamp=df['Donation_Date '] #= df['Donation_Date '].astype(np.int64)
df.index = df.Timestamp
#print(df.Timestamp) 
x=df.Timestamp
df1 = df.resample("D")
#train.Timestamp = pd.to_datetime(train.Datetime,format='%d-%m-%Y') 
train.Timestamp=train['Donation_Date ']
train.index = train.Timestamp 
train = train.resample("D").mean() 
test.Timestamp=test['Donation_Date ']
test.index = test.Timestamp 
test = test.resample("D").mean()
